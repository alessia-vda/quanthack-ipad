"""QA offline : contenu, prérequis, valeurs calculées, code Python, erreurs propres."""
import json
import math
import subprocess
import sys
from pathlib import Path
from calculs import VALUES
from server import evaluate

ROOT=Path(__file__).resolve().parent
rooms=json.loads((ROOT/'rooms.json').read_text(encoding='utf-8'))
assert [r['id'] for r in rooms]==[f'F{i}' for i in range(1,9)]
assert len(rooms)==8
seen=set()
tests=0
for r in rooms:
    assert len(r['objectifs']) in (2,3,4)
    assert len(r['rappel'])==2
    assert len(r['cours'])>=3 and all(x.get('titre') and x.get('html') for x in r['cours'])
    assert r['exemples_resolus'] and len(r['indices'])==3
    assert len(r['vocabulaire'])>=8
    assert r['writeup'] and r['question_entretien']['question'] and r['question_entretien']['reponse']
    assert r['references'] and r['validation']['valeurs_verifiees_par_script']
    assert r['validation']['relu_par'] is None
    assert all(p in seen for p in r['prerequis']), 'Prérequis acycliques'
    seen.add(r['id'])
    tasks=r['taches'];assert len(tasks)==7
    assert {t['type'] for t in tasks}=={'qcm','association','ordre','numerique','flag','code'}
    for i,t in enumerate(tasks):
        assert t.get('xp',0)>0
        if t['type']=='qcm':assert isinstance(t['reponse'],int) and 0<=t['reponse']<len(t['options'])
        if t['type']=='numerique':assert math.isclose(t['reponse'],VALUES[r['id']],rel_tol=0,abs_tol=1e-9),r['id']
        if t['type']=='association':assert len({p['definition'] for p in t['paires']})==len(t['paires'])
        if t['type']=='code':
            solution=evaluate(r['id'],i,t['solution'])
            starter=evaluate(r['id'],i,t['code_depart'])
            assert solution['passed']==solution['total']==len(t['tests']), (r['id'],solution)
            assert starter['passed']<starter['total'], (r['id'],starter)
            assert all('NotImplementedError' in row['detail'] for row in starter['results']),(r['id'],starter)
            tests+=2*solution['total']
print(f'OK · {len(rooms)} rooms · {sum(len(r["taches"]) for r in rooms)} tâches · {sum(len(r["vocabulaire"]) for r in rooms)} termes · {tests} comparaisons de tests Python (solutions + starters)')
