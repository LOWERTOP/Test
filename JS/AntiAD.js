/**
 * Shadowrocket 移除 twmanga.com & baozimh.com 相关正文插入广告
 * 作者: LOWERTOP
 */

// 确保 $response 存在
if (!$response || !$response.body) {
    $done({});
    return;
}

let modifiedBody = $response.body;

// **批量删除正文插入广告的 `class`**
const adClasses = ["mobadsq", "ad-container", "video-ad", "floating-banner", "popup-ads"];
adClasses.forEach(adClass => {
    const regex = new RegExp(`<div[^>]*class=["']?${adClass}["']?[^>]*>.*?<\\/div>`, "gis");
    modifiedBody = modifiedBody.replace(regex, '');
});

// **批量删除带有 `style="margin: 0px auto;"` 的广告**
modifiedBody = modifiedBody.replace(/<div[^>]*style=["']?margin:\s?0px\s?auto;["']?[^>]*>.*?<\/div>/gis, '');

// **删除 `div_adhost` 相关广告**
modifiedBody = modifiedBody.replace(/<div[^>]*class=["']?div_adhost["']?[^>]*>.*?<\/div>/gis, '');

// **返回修改后的 HTML**
$done({ body: modifiedBody });
