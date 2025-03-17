// 漫画网站广告屏蔽脚本
const body = $response.body;

// 只有在有响应体的情况下才执行
if (body) {
  try {
    // 获取当前域名
    const url = $request.url;
    const host = url.match(/https?:\/\/([^\/]+)/)[1];
    
    let html = body;
    
    // 针对不同网站的特定处理
    if (host.includes('twmanga.com')) {
      // 移除广告元素
      html = html.replace(/<div[^>]*class="?mobadsq"?[^>]*>[\s\S]*?<\/div>/gi, '');
      html = html.replace(/<div[^>]*class="?recommend"?[^>]*>[\s\S]*?<\/div>/gi, '');
      html = html.replace(/<div[^>]*style="overflow:hidden; flex: 1;"[^>]*>[\s\S]*?<\/div>/gi, '');
      
      // 移除广告相关脚本
      html = html.replace(/<script[^>]*src="[^"]*(?:ad|analytics|tracker)[^"]*"[^>]*>[\s\S]*?<\/script>/gi, '');
      
      // 移除内联广告脚本
      html = html.replace(/<script[^>]*>[\s\S]*?(?:ad|googlead|adsense)[\s\S]*?<\/script>/gi, '');
    }
    else if (host.includes('baozimh.com')) {
      // 移除广告元素
      html = html.replace(/<div[^>]*class="?recommend"?[^>]*>[\s\S]*?<\/div>/gi, '');
      html = html.replace(/<div[^>]*class="?footer"?[^>]*>[\s\S]*?<\/div>/gi, '');
      
      // 移除广告相关脚本
      html = html.replace(/<script[^>]*src="[^"]*(?:ad|analytics|tracker)[^"]*"[^>]*>[\s\S]*?<\/script>/gi, '');
      
      // 移除内联广告脚本
      html = html.replace(/<script[^>]*>[\s\S]*?(?:ad|googlead|adsense)[\s\S]*?<\/script>/gi, '');
    }
    
    // 通用处理：移除所有iframe
    html = html.replace(/<iframe[^>]*>[\s\S]*?<\/iframe>/gi, '');
    
    // 移除通用广告类名和ID
    html = html.replace(/<[^>]*(?:class|id)="[^"]*(?:ad|ads|banner|pop)[^"]*"[^>]*>[\s\S]*?<\/[^>]*>/gi, '');
    
    // 返回处理后的内容
    $done({body: html});
  } catch (err) {
    // 如果处理过程中出现错误，返回原始内容
    console.log('Error in comic-ads-blocker script: ' + err);
    $done({});
  }
} else {
  $done({});
}