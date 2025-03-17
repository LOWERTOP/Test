/**
 * Shadowrocket 移除 twmanga 相关网站的广告元素
 * 目标：删除 class="mobadsq" 及其他潜在广告
 * 适用于 twmanga 及其子域名
 */

if (!$response || !$response.body) {
    $done({});
    return;
}

let modifiedBody = $response.body;

// **匹配 `<div class="mobadsq">` 及其所有内容**
const adRegex = /<div[^>]*class=["']?mobadsq["']?[^>]*>[\s\S]*?<\/div>/gi;
modifiedBody = modifiedBody.replace(adRegex, '');

// **返回修改后的 HTML**
$done({ body: modifiedBody });