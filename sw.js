const CACHE_NAME = 'chic-table-v1';
const urlsToCache = [
  '/',
  '/static/logo_original.png',
  '/static/qr_code.png',
  '/static/capa_plato.png',
  '/static/capa_caraotas.png',
  '/static/capa_arroz.png',
  '/static/capa_carne.png',
  '/static/capa_tajadasi.png',
  '/static/capa_tajadasd.png'
];

self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(CACHE_NAME).then(function(cache) {
      return cache.addAll(urlsToCache);
    })
  );
});

self.addEventListener('fetch', function(event) {
  // Service Worker necesario para activar el prompt de instalación de PWA
  event.respondWith(
    fetch(event.request).catch(function() {
      return caches.match(event.request);
    })
  );
});