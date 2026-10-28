// Quants Court Studio — version 2026-10-28. Network-first for navigation to refresh installed apps.
const CACHE = 'quants-court-studio-v1';
const CORE = ['./','./index.html','./classic.html','./rooms.js','./app.js','./style.css','./manifest.webmanifest','./quants-court.svg'];
self.addEventListener('install', event => event.waitUntil(caches.open(CACHE).then(c => c.addAll(CORE)).then(() => self.skipWaiting())));
self.addEventListener('activate', event => event.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k !== CACHE && (k.startsWith('quanthack-') || k.startsWith('quants-court-'))).map(k => caches.delete(k)))).then(() => self.clients.claim())));
self.addEventListener('fetch', event => {
 const req = event.request; if(req.method !== 'GET') return; const url=new URL(req.url);
 if(url.origin !== location.origin) return;
 event.respondWith(fetch(req).then(res => {if(res.ok) {const copy=res.clone();caches.open(CACHE).then(c=>c.put(req,copy)).catch(()=>{});}return res;}).catch(()=>caches.match(req).then(hit=>hit|| (req.mode==='navigate'?caches.match('./index.html'):Response.error()))));
});
