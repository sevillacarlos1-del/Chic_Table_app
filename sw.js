if ('serviceWorker' in navigator) {
  window.addEventListener('load', function() {
    navigator.serviceWorker.register('/sw.js')
      .then(function(registration) {
        console.log('ServiceWorker registrado con éxito: ', registration.scope);
      })
      .catch(function(err) {
        console.log('Falla en el registro del ServiceWorker: ', err);
      });
  });
}