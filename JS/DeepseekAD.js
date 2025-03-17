// 定义需要屏蔽的规则
const rules = {
  "baozimh.com": [
    ".action-buttons.position-relative.chapter-goto",
    ".recommend",
    ".footer",
    "h3[style='margin: 0 0 12px; padding: 0;']"
  ],
  "twmanga.com": [
    ".ucfad_async",
    ".div_close_ads",
    ".mobadsq",
    "div[style='overflow:hidden; flex: 1;']",
    "div[style='width: 170px; margin: 0 auto; text-align: center;']",
    ".recommend",
    "#interstitial_fade"
  ]
};

// 执行元素移除操作
function removeElements() {
  const hostname = window.location.hostname;
  const selectors = rules[hostname] || [];
  
  selectors.forEach(selector => {
    document.querySelectorAll(selector).forEach(element => {
      element.remove();
    });
  });
}

// 监听页面变化（针对动态加载内容）
const observer = new MutationObserver(removeElements);
observer.observe(document, { childList: true, subtree: true });

// 初始执行
removeElements();
