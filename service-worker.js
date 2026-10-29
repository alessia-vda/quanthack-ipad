// Quants Court Studio — version 2026-10-28. Network-first for navigation to refresh installed apps.
const CACHE = 'quants-court-v68-cinq-cas-oral';
const CORE = ['./','./index.html','./classic.html','./rooms.js','./app.js','./style.css','./manifest.webmanifest','./quants-court.svg','./studio-upgrades.css','./studio-upgrades.js','./studio-rooms.js','./studio-rooms.css','./studio-f0.js','./studio-f0.css','./studio-alm.js','./studio-alm.css','./studio-alm-v66.css','./mascotte-quants-court.png','./quants-court-icon-192.png','./studio-pedago-v64.js','./studio-pedago-v64.css','./studio-world-news.js','./studio-world-news.css','./studio-v67.css','./studio-v67.js','./studio-v68.css','./studio-v68.js'];
self.addEventListener('install', event => event.waitUntil(caches.open(CACHE).then(c => c.addAll(CORE)).then(() => self.skipWaiting())));
self.addEventListener('activate', event => event.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k !== CACHE && (k.startsWith('quanthack-') || k.startsWith('quants-court-'))).map(k => caches.delete(k)))).then(() => self.clients.claim())));
self.addEventListener('fetch', event => {
 const req = event.request; if(req.method !== 'GET') return; const url=new URL(req.url);
 if(url.origin !== location.origin) return;
 event.respondWith(fetch(req).then(res => {if(res.ok) {const copy=res.clone();caches.open(CACHE).then(c=>c.put(req,copy)).catch(()=>{});}return res;}).catch(()=>caches.match(req).then(hit=>hit|| (req.mode==='navigate'?caches.match('./index.html'):Response.error()))));
});
