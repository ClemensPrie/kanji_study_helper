const CACHE = 'jsg-v2';
const ASSETS = [
    'index.html', 'manifest.json', 'icon.svg',
    'kanji_grade_1.html', 'kanji_grade_2.html', 'kanji_grade_3.html',
    'kanji_grade_4.html', 'kanji_grade_5.html', 'kanji_grade_6.html',
    'kanji_grade_s1.html', 'kanji_grade_s2.html', 'kanji_grade_s3.html',
    'vocab_n5.html', 'vocab_n4.html', 'vocab_n3.html',
    'vocab_n2.html', 'vocab_n1.html'
];

self.addEventListener('install', e => {
    e.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)));
    self.skipWaiting();
});

self.addEventListener('activate', e => {
    e.waitUntil(
        caches.keys().then(keys =>
            Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))
        )
    );
    self.clients.claim();
});

self.addEventListener('fetch', e => {
    e.respondWith(
        caches.match(e.request).then(r => r || fetch(e.request))
    );
});
