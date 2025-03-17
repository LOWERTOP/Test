(function() {
  const hostname = window.location.hostname;

  function hideElements(selector) {
    const elements = document.querySelectorAll(selector);
    elements.forEach(element => {
      element.style.display = 'none'; // 或者 element.remove(); 如果你想完全移除元素
    });
  }

  if (hostname.includes('baozimh.com')) {
    hideElements('.action-buttons.position-relative.chapter-goto');
    hideElements('.recommend');
    hideElements('.footer');
    hideElements('h3[style="margin: 0 0 12px; padding: 0;"]');
  } else if (hostname.includes('twmanga.com')) {
    hideElements('.ucfad_async');
    hideElements('.div_close_ads');
    hideElements('.mobadsq');
    hideElements('div[style="overflow:hidden; flex: 1;"]');
    hideElements('div[style=" width: 170px; margin: 0 auto; text-align: center;"]');
    hideElements('.recommend');
    hideElements('#interstitial_fade'); // 注意：这里是 ID 选择器，使用 #
  }
})();
