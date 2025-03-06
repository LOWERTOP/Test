[![Shadowrocket](https://socialify.git.ci/LOWERTOP/Shadowrocket/image?custom_description=%E4%BD%BF%E7%94%A8%E6%89%8B%E5%86%8C%0AUser+Manual&description=1&font=Rokkitt&forks=1&logo=https%3A%2F%2Fraw.githubusercontent.com%2FLOWERTOP%2FShadowrocket-First%2Frefs%2Fheads%2Fmain%2Fimg%2FShadowrocket.png&name=1&pattern=Plus&stargazers=1&theme=Light)](https://github.com/LOWERTOP/Shadowrocket)

[![README in English](https://img.shields.io/static/v1?label=&message=README%20in%20English&color=blue&logo=googletranslate&logoColor=white&labelColor=blue&messageColor=white)](https://translate.google.com/translate?hl=en&sl=zh-CN&tl=en&u=https://lowertop.github.io/Shadowrocket "Google Translate")

> [!NOTE]
> 
> The original Lazy config files and the keyword list repository has become inactive. This repository will maintain its final version or possible subsequent versions and plans to gradually refine the original keyword list into a user manual for reference. The [Original branch](https://github.com/LOWERTOP/Shadowrocket/tree/Original) contains the original files, which can be accessed for review. The Lazy configuration provided by the [Johnshall repository](https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever) will also continue to be updated based on the files in this repository. If you have other requirements, you may try checking **[Color Schemes & Configs Repository](https://github.com/LOWERTOP/Shadowrocket-First)**. <br>
> This repository, as an ordinary user, expresses sincere gratitude to the original author and all contributors to the related projects!

------

# [Shadowrocket User Manual](https://lowertop.github.io/Shadowrocket/ "Release Page")

> [!NOTE]
> 
> **[Shadowrocket](https://apps.apple.com/us/app/shadowrocket/id932747118) (commonly referred to as "Little Rocket")** is a network proxy tool developed by **[Shadow Launch Technology Limited](https://shadowlaunch.com/)** specifically for iOS devices. It also supports Apple TV and Mac devices (M-series chips). Shadowrocket offers flexible configuration options, enabling users to route their device’s network traffic through a proxy server, helping to bypass specific network environments, access restricted content, and enhance online privacy protection, meeting various user needs.

> [!TIP]
> 
> **Quick Usage Guide**
> 
> > * Home > Add Node
> > * Settings > Latency Test Method > **`CONNECT`**
> > * Home > Connectivity Test, then select an available node to connect
> 
> When launching for the first time, you will be prompted to **`install the VPN configuration file`**, please tap **`OK`** and **`Allow`** to ensure normal usage.


## [Table of Contents](#table-of-contents)
> [!TIP]
> * Click on a **section title** to quickly navigate to the corresponding content.
> * Click on a **blue title** in the content to quickly return to the table of contents.

> * [Home](#home)
>     * [Add Node](#add-node)
>     * [Add WireGuard Node](#add-wireguard-node)
>     * [Update Subscription Nodes](#update-subscription-nodes)
>     * [Sort Nodes](#sort-nodes)
>     * [Share and Manage Nodes](#share-and-manage-nodes)
>     * [Filter Subscription Nodes](#filter-subscription-nodes)
>     * [Proxy Through/Proxy Chain](#proxy-through-proxy-chain)
>     * [Global Routing Differences](#global-routing-differences)
>     * [Connectivity Test](#connectivity-test)
>     * [Modify Test Address](#modify-test-address)
>     * [Scenarios](#scenarios)
>     * [Simple Mode](#simple-mode)
>     * [Enable Fallback](#enable-fallback)
> * [Configuration](#configuration-page)
>     * [Configuration Files](#configuration-files)
>     * [Using Configurations](#using-configurations)
>     * [Edit Configuration](#edit-configuration)
>     * [Edit Plain Text](#edit-plain-text)
>     * [Preview Configuration](#preview-configuration)
>     * [Update Configuration](#update-configuration)
>     * [Rename](#rename)
>     * [Export Configuration](#export-configuration)
>     * [Extended Configuration](#extended-configuration)
>     * [General Parameters](#general-parameters)💡
>     * [Add Rules](#add-rules)
>     * [Rule Priorities](#rule-priorities)
>     * [Rule Types](#rule-types)
>     * [Rule Strategies](#rule-strategies)
>     * [APP-Based Traffic Routing](#app-based-traffic-routing)
>     * [Update Rule Sets](#update-rule-sets)
>     * [Preview Rule Sets](#preview-rule-sets)
>     * [Modify DNS](#modify-dns)
>     * [DNS-over-PROXY](#dns-over-proxy)
>     * [Function of no-resolve](#function-of-no-resolve)
>     * [Proxy Groups/Strategy Groups](#proxy-groups-strategy-groups)
>     * [Proxy Group Types](#proxy-group-types)
>     * [Script URL](#script-url)
>     * [Rule Set URL](#rule-set-url)
>     * [Copy Configuration File](#copy-configuration-file)
>     * [Hosts](#hosts)
>     * [URL Rewrite](#url-rewrite)
>     * [HTTPS Decryption](#https-decryption)
>     * [Load Balancing](#load-balancing)
>     * [Modules](#modules)
>     * [Certificate Module](#certificate-module)
>     * [Identity Certificate Password](#identity-certificate-password)
> * [Data](#data-page)
>     * [Proxy Logs](#proxy-logs)
>     * [DNS Logs](#dns-logs)
>     * [iCloud Auto Sync](#icloud-auto-sync)
>     * [Node Data Management](#node-data-management)
>     * [Traffic Statistics](#traffic-statistics)
> * [Settings](#settings-page)
>     * [Latency Test Method](#latency-test-method)
>     * [Widgets](#widgets)
>     * [Connect on Demand](#connect-on-demand)
>     * [Tunnels](#tunnels)
>     * [Upstream Proxy](#upstream-proxy)
>     * [Proxy Sharing](#proxy-sharing)
>     * [Proxy Detection](#proxy-detection)
>     * [Proxy Types](#proxy-types)
>     * [Enable UDP Forwarding](#enable-udp-forwarding)
>     * [Hide VPN Icon](#hide-vpn-icon)
>     * [GEOIP Database](#geoip-database)
>     * [Auto Update](#auto-update)
>     * [Mild Policy Mechanism](#mild-policy-mechanism)
> * [Others](#other-issues)
>     * [Auto Switch Nodes](#auto-switch-nodes)
>     * [SSL Errors](#ssl-errors)
>     * [Node Flags](#node-flags)
>     * [Node Exclamation Marks](#node-exclamation-marks)
>     * [WeChat Spinning](#wechat-spinning)
>     * [Modules Disappeared](#modules-disappeared)
>     * [Modules Invalid](#modules-invalid)
>     * [VPN Auto Disconnect](#vpn-auto-disconnect)
>     * [Location Permission](#location-permission)
>     * [Compilation Reasons](#compilation-reasons)
>     * [Download Shadowrocket](#download-shadowrocket)
>     * [URL-Schemes](#url-schemes)

------

## [Home](#home)

### [Add Node](#table-of-contents)

> * Home > Top Left Corner > Scan QR Code to Add
>   
> * Copy the node link, such as `trojan://*` `vmess://*` `vless://*`, and it will be automatically recognized and imported when opening Shadowrocket.
>   
>   `Clipboard reading permission must be enabled`
> 
> * Home > Top Right Corner `➕` > Type `Subscribe` > Enter subscription URL in the URL field > Save
> 
>   `Appending "#1", "#2", "#3", etc., to the subscription URL allows repeated additions of the same subscription`
> 
> * Home > Top Right Corner `➕`, select the corresponding node type, fill in the node configuration information, and save.
> 
>   **Protocols supported by Shadowrocket**: `Shadowsocks, ShadowsocksR, Subscribe, Vmess, VLESS, Relay, Socks5, Socks5 Over TLS, HTTP, HTTPS, HTTP2, Trojan, Hysteria, Hysteria2, TUIC, Juicity, WireGuard, Snell v2, Brook, Lua`

### [Add WireGuard Node](#table-of-contents)

> * Home > Top Right Corner `➕` > Select `WireGuard` as type, and fill in the configuration details.
> 
> * Copy the `WireGuard` configuration in the following format, and when opening Shadowrocket, a prompt to add will automatically appear. Click to add.
>   
>   ```ruby
>   [Interface]
>   PrivateKey = xxxxxx
>   Address = 172.16.0.2/32
>   DNS = 1.1.1.1
>   MTU = 1420
>   [Peer]
>   PublicKey = xxxxxx
>   AllowedIPs = 0.0.0.0/0
>   AllowedIPs = ::/0
>   Endpoint = engage.cloudflareclient.com:2408
>   Reserved = 12,34,56
>   ```
>   If the dialog does not appear automatically, it might be due to the `Allow Clipboard Detection` setting being disabled. You can re-enable it or manually add the configuration by clicking the `Paste` button under `Connectivity Test` on the home page.

### [Update Subscription Nodes](#table-of-contents)

> * Swipe right on the subscription > Update
> 
> * Click the refresh subscription button 🔄 on the home page
> 
> * Settings > Subscription > Update on Open (Closing the app completely and reopening it will automatically update the subscription)
> 
> * Settings > Subscription > Automatic Background Update (Requires enabling Shadowrocket in system `Settings > General > Background App Refresh`, with an update interval of 1-24 hours)
> 
> * Shadowrocket provides a `Update Subscription` shortcut for automation.
> 
> * Long press the app icon on the home screen > Update Subscription
>   
> 
> **Reasons for Subscription Add/Update Errors**:
> * **forbidden** indicates that the subscription has been reset or the token is incorrect.
> * **not found** indicates a path error.
> * **service unavailable** indicates a domain error or the domain is blocked by the ISP.

### [Node Sorting](#Usage Directory)

> Settings > Subscription > Sort by `Ping`

### [Node Sharing and Organization](#Usage Directory)

> **Node Sharing**
> 
> > * Long press the node > Copy to share the node link with other devices
> > 
> > * Swipe left on the node > QR code, other devices can add the node by scanning the QR code (Click the `Share` button in the top right corner on the QR code page to share the QR code in other formats)
> > 
> >   `There is no unified standard for node QR codes. For some protocols like Vmess, when using other proxy tools to scan the QR code, some node information might be lost, causing connection issues. If this happens, carefully check if the node configurations are consistent.`
> > 
> > * Click the `ⓘ` icon next to the node, scroll to the bottom of the page, and there are various options to share the node.
> > 
> > * Expand the node list, click the edit button `•••` under connectivity test, select the nodes you want to share, and click the copy button in the top left corner to share multiple node links.
> 
> **Node Organization**
> 
> > * **Rearrange**: Click the edit button `•••`, long press the `≡` icon next to the subscription to rearrange the order of subscriptions (local nodes are placed at the top by default)
> > 
> > * **Node Classification**: Nodes added manually will be categorized as `Local Nodes` by default. If you want to reclassify local nodes, you can use the `Fold` feature. Click the edit button `•••`, select the nodes, click `Fold` in the top left corner, and give a name to the new node category (the `Fold` feature can be applied to both local nodes and subscription nodes).
> > 
> > * **Delete Nodes**: Click the edit button `•••`, click `Delete` in the top left corner to delete all nodes or delete nodes with timeout issues from the connectivity test results.
> > 
> > * **Swipe Menu**: Swipe right on a subscription to test its connectivity or update it. Swipe right on a node to test its connectivity or copy it. This allows you to add a new node with the same configuration in the node list.

### [Subscription Node Filtering](#Usage Directory)

> **Node Filtering**
> 
> > Home > Click the `ⓘ` icon next to Subscription > Filter
> > 
> > `The regular expression for grouping and proxy grouping works the same as the commands below, but the slashes `/` at the beginning and end need to be removed.`
> > 
> > * Keep nodes whose names contain both keywords A and B:
> >   ```ruby
> >   /(?=.*(A))^(?=.*(B))^.*$/
> >   ```
> > * Keep nodes whose names contain either keyword A or B:
> >   ```ruby
> >   A|B
> >   ```
> > * Exclude nodes whose names contain either keyword A or B:
> >   ```ruby
> >   /^((?!(A|B)).)*$/
> >   ```
> > * Keep nodes whose names contain keyword A but exclude keyword B:
> >   ```ruby
> >   /(?=.*(A))^((?!(B)).)*$/
> >   ```
> 
> **Batch Organization**
> 
> > The node subscription filter feature supports using script code to batch organize and modify specific subscription node settings and node names.
> > 
> > * Batch replace keyword `a` with keyword `b` in node names:
> >   ```ruby
> >   $server.title=$server.title.replace(/a/g,'b')
> >   ```
> > * Batch add the prefix `abc` to node names:
> >   ```ruby
> >   $server.title='abc'+$server.title
> >   ```
> > * Batch enable reserved slots for all nodes:
> >   ```ruby
> >   $server.reserved="1,40-60,30-50"
> >   ```
> > * Batch enable multiplexing for all nodes:
> >   ```ruby
> >   $server.mux=1
> >   ```
> > * Batch set proxy chain/chain proxy for all subscription nodes:
> >   ```ruby
> >   $server.chain="SubscriptionName/NodeName"
> >   ```
> >   ```ruby
> >   $server['dialer-proxy']="UUIDValue"
> >   ```
> >   `The first command is for official use, the second command is temporary, and in the transitional period, the valid one takes precedence. The "UUIDValue" can be copied from the middle node or subscription JSON text. The "SubscriptionName/NodeName" can also use the UUID value.`
> 
> **Other Commands**
> 
> > This feature also supports more complex script instructions. Please refer to [this example](https://github.com/LOWERTOP/Shadowrocket-First#%E7%AD%9B%E9%80%89%E8%AE%A2%E9%98%85%E8%84%9A%E6%9C%AC) for details.

### [Proxy Through/Proxy Chain](#Usage Directory)

> The current proxy connects through another proxy, supporting multi-level chained proxies. To use proxy chaining:
> 
> * Use node A to connect, click the `ⓘ` icon next to node A, choose proxy through node B. The traffic will flow: `Client > B > A > Web server`
> * You can use the entire subscription as a proxy chain, and the effective node will be randomly selected from the nodes in the subscription. The actual active node can be confirmed by searching for `backend chain` in the VPN logs.
> * Supports batch modification of proxy chain for subscription nodes to implement multiple chained proxy deployments. Specific commands can be found in [Subscription Node Filtering > Batch Organization](#Subscription Node Filtering).
> * To cancel the proxy through/proxy chain: Click the node's `ⓘ` icon, choose `Cancel` in the top right corner after the proxy through, and save.

### [Global Route Differences](#Usage Directory)

> * **Configuration**: Traffic is allocated according to preset rules, some are routed through nodes, others are not.
> * **Proxy**: All traffic is routed through the same node.
> * **Direct Connection**: All traffic bypasses nodes and connects directly.
> * **Scenario**: Automatically switches to the pre-set routing mode based on different network connection types (Wi-Fi, cellular data), and selects the corresponding configuration file and node connection.

### [Connectivity Test](#Usage Directory)

> Click on the `Connectivity Test` on the homepage, the node list will display the latency in milliseconds (ms), which is the transmission time for data packets. Different `Latency Test Methods` correspond to different calculation results. Long press the `Connectivity Test` to temporarily adjust the test method, which will only apply to this test.
> 
> Settings > Latency Test Method
> 
> * **TCP**: Round trip time for establishing a `TCP` connection.
> * **ICMP**: Round trip time for sending `ICMP` echo request and receiving `ICMP` echo reply.
> * **CONNECT**: Sends an `HTTP HEAD` request to the test URL, measuring the round trip time from sending the request to receiving the response headers.
> 
> It’s recommended to choose `CONNECT` as it provides a more accurate reflection of node connectivity. Latency size does not directly correlate to upload/download speed, for which other tools like <https://www.speedtest.net> should be used.

### [Modify Test Address](#Usage Directory)

> **For latency testing on the homepage and grouped nodes**
> 
> > * Settings > Latency Test Method > URL Test Settings
> > * Homepage > Connectivity Test's circular icon > URL Test Settings
> 
> **For latency testing on proxy grouped nodes**
> 
> > * Click the `ⓘ` icon in the configuration file > Proxy Group > Edit or add a group with automatic test type > Enter the URL at the bottom.

### [Scenario](#Usage Directory)

> A scenario automatically switches to a pre-configured routing mode based on different network connection types (Wi-Fi, cellular data) and selects the corresponding configuration file and node connection.
> > * Homepage > Global Route > Set `Scenario` > Add Scenario
> > * Set the routing mode (`Configuration`, `Direct Connection`, `Proxy`) for specific network connection types (`Node`, `Group`), configuration files, and remarks.
> > * Network connection types: Wi-Fi, cellular data, default. For Wi-Fi, the SSID must be filled in with the Wi-Fi name.
> > * Homepage > Global Route > Select `Scenario`
>
> The software supports adding scenarios for cellular data and supports using the `Network Interface` as a matching condition:
> > * Default (blank) represents interface `pdp_ip0`
> > * When the device enables multiple cellular networks, you can check the corresponding interface info in Shadowrocket's Settings > Diagnostics > Network.
> > * Input format: `pdp_ip1`, `pdp_ip2`, `pdp_ip3`, etc.
> 
> When adding a scenario for the first time, a permissions request dialog may pop up. For more details, refer to [Location Permissions](#Location Permissions). If location permissions are not granted, the ✅ mark on the scenario list will not automatically switch with network type changes, but this does not affect the normal function of scenarios.
> 
> 设置 > 隧道/按需求连接 中的 `包含所有网络` 相关选项可能会对场景模式的生效造成影响


### [简单模式](#使用目录)

> 简单模式是一种以相对简单的方式实现自动测试并选择延迟低的节点进行连接的设置模式
> 
> * 首页 > 全局路由 > 分组 > 简单模式

> **节点的范围是什么？**
> > 当开启简单模式，此时下方会出现分组选项，如果没有继续添加分组的操作，节点范围就是首页全部节点，如果添加分组，范围就变成分组里的节点
> 
> **自动测试的周期是多久？延迟低的判断依据是什么？**
> > `设置 > 延迟测试方法 > URL测试设置`，这里规定了测试的间隔时间，默认 600s，即表示每 10 分钟自动进行一次节点延迟测试。相邻两次测试结果中最小延迟值的对比，根据公差机制决定是否切换节点，公差越大，触发节点切换的频次越低，默认 0ms，即表示只要后面测试结果的最低延迟节点比前面测试结果的最低延迟节点延迟小就会自动切换
> 
> **切换的节点给什么规则使用？**
> > Shadowrocket 内置策略 `proxy`，简单模式时自动切换的节点使用于所有指向 `proxy` 策略的规则
> 
> **简单模式是自动切换延迟低节点，代理分组的 url-test 类型也是自动切换延迟低节点，两者有何不同？**
> > 代理分组创建后，需要在规则中修改策略指向，而简单模式已经关联 `proxy` 策略，节省了修改规则的步骤<br>
> > `全局路由` 选择 `代理` 时将导致所有 `代理分组` 失效，而简单模式依然能够实现自动切换节点
> 
> **添加分组时，`测速` 开关是什么作用？**
> > 开启测速，这个分组才允许自动切换节点。不开启测速，这个分组只能手动选择节点

### [启用回退](#使用目录)

> 首页 > 全局路由 > 启用回退
> 
> `启用回退` 的功能是当节点连接失败时自动切换其他可用节点
> * 连接失败3次才会触发回退机制
> * 节点只满足可用性，不要求是最低延迟节点
> * 随机切换，不按照节点顺序选择
> * 策略为 `proxy`，节点切换范围就是首页全部节点，如果开启简单模式并选择分组，则范围缩小至分组内节点
> * 策略为 `非 select 类型` 的分组/代理分组，节点切换范围就是分组或代理分组内节点
> * 具体切换到哪个节点，请查看 [代理日志](#代理日志)

------

## [配置页面](#配置页面)

### [配置文件](#使用目录)

> Shadowrocket 的配置文件（通常以 .conf 格式存在）主要用于快速设置和软件的主要功能，简化用户手动配置的流程。配置文件还可以在多设备间同步以及分享配置文件给其他用户，以快速部署相同设置<br>
> Shadowrocket 内置了一个默认配置文件 `default.conf`，其中包含了国内外主要网站或服务的分流规则，一般可以满足大多数用户的基本需求。此配置文件的内容跟随应用更新而做不定期的调整。如果在使用过程中错误修改或误删配置文件，可以点击 `配置` > `恢复默认配置`。
> 
> 添加配置文件方法：
> > * 从 URL 下载配置
> >   * 配置 > 右上角 `➕` > 粘贴配置链接 > 下载 > 点击对应的配置文件 > 使用配置
> >   * Shadowrocket兼容使用 `Clash YAML 格式` 的配置文件。使用含节点信息的标准 Clash 链接可以同时导入配置文件和节点信息
> >  
> > * 从本地存储或云盘导入
> >   * 配置 > 从云导入，点击对应存储路径的配置文件
> 
> 点击配置文件，显示操作菜单：
> > * [使用配置](#使用配置)
> > * [编辑配置](#编辑配置)
> > * [编辑纯文本](#编辑纯文本)
> > * [预览配置](#预览配置)
> > * [更新配置](#更新配置)
> > * [扩展配置](#扩展配置)
> > * [重新命名](#重新命名)
> > * [导出配置](#导出配置)
> 
> 点击配置文件的 `ⓘ` 图标，进入编辑菜单：
> > * [通用](#通用参数)
> > * [规则](#添加规则)
> > * [Hosts](#hosts)
> > * [URL重写](#url重写)
> > * [HTTPS解密](#https解密)
> > * 脚本
> > * [代理分组](#代理分组策略组)
> > * [脚本URL](#脚本url)
> > * [规则集URL](#规则集url)
> > * [复制](#复制配置文件)
> > * 替换策略
> > * 测试规则

### [使用配置](#使用目录)

> 点击 `使用配置` 可以启用该配置文件，也可以使用该按钮对当前生效的远程规则集、脚本等远程资源进行更新

### [编辑配置](#使用目录)

> 使用 UI 交互界面对配置文件的可设置项进行调整。部分设置或命令不提供 UI 编辑界面，如有需要可在 [纯文本编辑](#编辑纯文本) 中使用

### [编辑纯文本](#使用目录)

> 使用纯文本模式对配置文件的可设置项进行调整。部分设置或命令不提供 UI 编辑界面，仅在纯文本模式下可以设置
> 
> 配置文件的纯文本编写方法，请参考：
> > * [懒人配置](https://raw.githubusercontent.com/LOWERTOP/Shadowrocket/main/lazy.conf)<br>
> > * [懒人配置（含策略组）](https://raw.githubusercontent.com/LOWERTOP/Shadowrocket/main/lazy_group.conf)

### [预览配置](#使用目录)

> 查看配置文件的纯文本格式。该选项仅当配置文件是以远程配置文件的形式添加进来的才会出现

### [更新配置](#使用目录)

> 更新当前配置文件以及当前所用的规则集、脚本等远程资源。该选项仅当配置文件是以远程配置文件的形式添加进来的才会出现。软件同时提供自动更新功能，详细更新设置技巧请参见 [自动更新](#自动更新) 词条

### [重新命名](#使用目录)

> 重命名当前配置文件

### [导出配置](#使用目录)

> 将当前配置文件以文件的形式导出

### [扩展配置](#使用目录)

> * 从配置 a 扩展出配置 b，此时默认关系是 b 包含 a，也可以理解为 b 继承了 a 的内容
> 
> * 配置 b 优先级高于配置 a，该功能是对配置建立包含关系，以满足同时使用多个配置的需求
> 
> * 点击配置文件的 `ⓘ` 图标 > 通用 > 包含配置，可以修改或解除包含关系

### [通用参数](#使用目录)

> **旁路系统（bypass-system）**：如果禁用此选项，可能会导致一些系统问题，如推送通知延迟
> 
> **跳过代理（skip-proxy）**：此选项强制域名或IP的连接范围由 Shadowrocket `TUN 接口` 来处理，而不是 Shadowrocket 代理服务器。此选项用于解决一些应用程序的一些兼容性问题
> 
> **TUN旁路路由（tun-excluded-routes）**：Shadowrocket `TUN接口` 只能处理 `TCP 协议`。使用此选项可以绕过指定的IP范围，让其他协议通过
> 
> **DNS覆写（dns-server）**：使用普通 DNS 或加密 DNS（如 `doh` `doq` `dot` 等）覆盖默认的系统 DNS。有些 `dns over https` 支持 `http3`，所以尝试查询，如果支持就切换到 `http3`，可在 `doh链接` 后面加上 `#no-h3` 关闭。`doh` 强制通过 `h3` 查询的写法是将 `https` 改成 `h3`，如`h3://dns.alidns.com/dns-query`
> 
> **备用DNS（fallback-dns-server）**：当覆写 DNS 查询失败或查询时间超过2秒，Shadowrocket 会自动回退备用 DNS。如需指定多个 DNS，可用逗号分隔。`system` 表示回退到系统 DNS
> 
> **启用IPv6支持（ipv6）**：`false` 表示不启用，`true` 表示启用。即使不启用此选项，当本地网络环境支持 IPv6，并且节点域名支持 IPv6 解析，Shadowrocket 也会使用节点的 IPv6 地址进行访问。解决方法是关闭节点域名的 IPv6 解析，或者在配置文件的 `[Host]` 项目下为节点域名指定 IP 地址
> 
> **首选IPv6（prefer-ipv6）**：优先向 IPv6 的 DNS 服务器查询 `AAAA` 记录，优先使用 `AAAA` 记录。`false` 表示不启用
> 
> **私有IP应答（private-ip-answer）**：如果不启用该选项，域名解析返回私有 IP，Shadowrocket 会认为该域名被劫持而强制使用代理
> 
> **TUN包含路由（tun-included-routes）**：默认情况下，Shadowrocket 接口会声明自己为默认路由，但由于 Wi-Fi 接口的路由较小，有些流量可能不会通过 Shadowrocket 接口。使用此选项可以添加一个较小的路由表
> 
> **总是真实IP（always-real-ip）**：这个选项要求 Shadowrocket 在 `TUN` 处理 DNS 请求时返回一个真实的 IP 地址而不是假的IP地址
> 
> **DNS劫持（hijack-dns）**：有些设备或软件总是使用硬编码的 DNS 服务器，例如 Netflix 通过 Google DNS（`8.8.8.8` 或 `8.8.4.4`）发送请求，您可以使用此选项来劫持查询
> 
> **包含配置（include）**：表示当前配置包含另一个配置的内容，当前配置的优先级高于被包含配置。该选项是对配置建立包含关系，以满足同时使用多个配置的需求
> 
> 💡 **dns-direct-system**：直连的域名类规则使用系统 DNS 进行查询。`false` 表示不启用
> 
> 💡 **icmp-auto-reply**：ping 数据包自动回复
> 
> 💡 **always-reject-url-rewrite**：不开启时，「重写的REJECT策略」默认只有在配置模式下生效。开启后，可以令该策略在其他全局路由模式下都生效
> 
> 💡 **dns-direct-fallback-proxy**：直连域名解析失败后使用代理。`false` 表示不启用
> 
> 💡 **udp-policy-not-supported-behaviour**：当 UDP 流量匹配到规则里不支持 UDP 转发的节点策略时重新选择回退行为，可选行为包括 `DIRECT` `REJECT`。`DIRECT` 表示直连转发 UDP 流量，`REJECT` 表示拒绝转发 UDP 流量
>
> 💡 **stun-response-ip**：此选项包含两个命令：`stun-response-ip` 和 `stun-response-ipv6`。该选项允许返回一个虚假的IP地址，如 `stun-response-ip=1.1.1.1`  `stun-response-ipv6=::1`，目的是防止真实IP地址泄漏，提高 WebRTC 的隐私和安全性
>
> 💡 **compatibility-mode**：网络兼容模式。`0 > 禁用`；`1 > Proxy with Loopback Address`；`2 > Proxy Only`；`3 > TUN Only`。当参数的值设定为3时的效果等同于：设置 > 代理 > 代理类型 > None
>
> 💡 **always-ip-address**：强制所有域名使用本地 DNS 解析。设置为 `true` 表示启用。（此参数为隐藏属性，建议谨慎设置，可能导致相关域名的 CDN 失效。）
> 
> `带💡符号的参数只能通过配置文件的纯文本模式进行设置，没有 UI 操作选项`

### [添加规则](#使用目录)

> 在 Shadowrocket 中，"规则"是指用来决定哪些网络请求应该走代理、哪些请求应该直接连接互联网的规则集合。规则通常是基于用户的需求来配置 [规则策略](#规则策略)，目的是实现对流量的精细控制
> 
> * 点击配置文件的 `ⓘ` 图标 > 规则 > 右上角 `➕`，根据需求选择 [规则类型](#规则类型) 和 [规则策略](#规则策略)，填写规则内容
> 
> * 数据 > 代理 > 启用日志记录，产生网络活动后回到该页面，从最近的日志中查看网络活动记录，点击任一记录查看详情，点击右上角 `•••` 选择类型添加规则
> 
> * 规则匹配需要着重注意 [规则的优先级](#规则优先级) 顺序

### [规则优先级](#使用目录)

> 规则的匹配是从上到下逐条匹配的，一旦匹配到某条规则，Shadowrocket 就会停止继续匹配。因此，规则的顺序非常重要，优先级高的规则应该放在前面
>
>   * 上面的规则优先于下面的规则
>   * 域名类的规则优先于IP类规则
>   * 模块中的规则优先于配置文件

### [规则类型](#使用目录)

> **DOMAIN-SUFFIX**：匹配请求域名的后缀
> 
> > 如 `DOMAIN-SUFFIX,example.com,DIRECT` 可以匹配到 `a.example.com` `a.b.example.com`
> 
> **DOMAIN-KEYWORD**：匹配请求域名的关键词
> 
> > 如 `DOMAIN-KEYWORD,exa,DIRECT` 可以匹配到 `a.example.com` `a.b.example.com`
> 
> **DOMAIN**：匹配请求的完整域名
> 
> > 如 `DOMAIN,www.example.com,DIRECT` 只能匹配到 `www.example.com`
> 
> **USER-AGENT**：匹配用户代理字符串，支持使用通配符`*`
> 
> > 如 `USER-AGENT,MicroMessenger*,DIRECT` 可以匹配到 `MicroMessenger Client`
> 
> **URL-REGEX**：匹配 URL 正则式
> 
> > 如 `URL-REGEX,^https?://.+/item.+,REJECT` 可以匹配到 `https://www.example.com/item/abc/123`
> 
> **IP-CIDR**：匹配 IPv4 或 IPv6 地址
> 
> > 如 `IP-CIDR,192.168.1.0/24,DIRECT` 可以匹配到IP段 `192.168.1.1～192.168.1.254`。当域名请求遇到IP类规则时，Shadowrocket会向本地DNS服务器发送查询请求，以判断主机IP是否匹配规则。若IP类规则加 `no-resolve`（如：`IP-CIDR,172.16.0.0/12,DIRECT,no-resolve`），则域名请求将会跳过此规则，不会触发本地DNS查询
> 
> **IP-ASN**：匹配 IP 地址隶属的 ASN 编号
> 
> > 如 `IP-ASN,56040,DIRECT` 可以匹配到属于China Mobile Communications Corporation网络的IP地址
> 
> **RULE-SET**：匹配规则集内容。规则集的组成部分需包含规则类型
> 
> **DOMAIN-SET**：匹配域名集内容。域名集的组成部分不包含规则类型
> 
> **SCRIPT**：匹配脚本名称
> 
> **DST-PORT**：匹配目标主机名的端口号
> 
> > 如 `DST-PORT,443,DIRECT` 可以匹配到 443 目标端口
>   
> **GEOIP**：匹配 IP 数据库
> 
> > 如 `GEOIP,CN,DIRECT` 可以匹配到归属地为CN的IP地址
> 
> **FINAL**：兜底策略
> 
> > 如 `FINAL,PROXY` 表示当其他所有规则都匹配不到时才使用 `FINAL` 规则的策略
> 
> **AND**：逻辑规则，与规则
> 
> > 如 `AND,((DOMAIN,www.example.com),(DST-PORT,123)),DIRECT` 可以匹配到 `www.example.com:123`
> 
> **NOT**：逻辑规则，非规则
> 
> > 如 `NOT,((DST-PORT,123)),DIRECT` 可以匹配到除了 `123` 端口的其他所有请求
> 
> **OR**：逻辑规则，或规则
> 
> > 如 `OR,((DST-PORT,123),(DST-PORT,456)),DIRECT` 可以匹配到 `123` 或 `456` 端口的所有请求
> 
> **PROTOCOL**：匹配传输协议类型
> 
> > `PROTOCOL` 类型不支持单独使用，只能作为子规则类型嵌套于逻辑规则当中。如 `AND,((PROTOCOL,UDP),(DST-PORT,443)),REJECT-NO-DROP`

### [规则策略](#使用目录)

> **PROXY**：代理。通过代理服务器转发流量
> 
> **DIRECT**：直连。连接不经过任何代理服务器
> 
> **REJECT**：拒绝。返回 HTTP 状态码 404，没有内容
> 
> **REJECT-DICT**：拒绝。返回 HTTP 状态码 200，内容为空的JSON对象
> 
> **REJECT-ARRAY**：拒绝。返回 HTTP 状态码 200，内容为空的JSON数组
> 
> **REJECT-200**：拒绝。返回 HTTP 状态码 200，没有内容
> 
> **REJECT-IMG**：拒绝。返回 HTTP 状态码 200，内容为 1 像素 GIF
> 
> **REJECT-TINYGIF**：拒绝。返回HTTP状态码200，内容为 1 像素 GIF
> 
> **REJECT-DROP**：拒绝。丢弃 IP 包
> 
> **REJECT-NO-DROP**：拒绝。返回 ICMP 端口不可达
> 
> 除此之外，规则策略还可以选择 `代理分组` `订阅名称` `分组` `服务器节点`

### [APP分流](#使用目录)

> 根据不同 App 或特定服务指定分流规则，并使其按照设定的规则执行代理策略
> 
> 示例：YouTube App 分流走代理
> 
> * 复制 YouTube 的规则集链接
>   ```ruby
>   https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/YouTube/YouTube.list
>   ```
> * 点击配置文件的 `ⓘ` 图标 > 规则 > 右上角 `➕`，类型选择 `RULE-SET`，策略选择 `PROXY`，输入框内粘贴 `规则集链接`，保存完成（策略可以根据需求使用其他选项）
> 
> iOS系统没有常规分应用代理的操作，只能通过 `域名 / ip / ua` 规则实现app分流效果。可自行抓包，或者订阅 [blackmatrix7](https://github.com/blackmatrix7) 的 [规则集](https://github.com/blackmatrix7/ios_rule_script/tree/master/rule/Shadowrocket)。如果引用的链接是域名集，添加规则时，类型请选择 `DOMAIN-SET`

### [更新规则集](#使用目录)

> * 手动更新：点击配置文件 > 使用配置
> * 自动更新：[自动更新](#自动更新)

### [预览规则集](#使用目录)

> 点击配置文件 > 编辑配置 > 规则 > 在规则集上左滑 > 预览

### [修改DNS](#使用目录)

> **DNS覆写**
>   
> >   点击配置文件的 `ⓘ` 图标 > 通用 > DNS 覆写<br>
> >   使用普通 DNS 或加密 DNS（如 DoH、DoQ、DoT 等）覆盖默认的系统 DNS。填 system 表示使用系统 DNS。也支持使用 [通过代理转发 DNS 查询请求](#dns-over-proxy)
> >   
> >   **普通 DNS 示例**<br>
> >   ```ruby
> >   dns-server = 223.5.5.5,119.29.29.29
> >   ```
> >   
> >   **加密 DNS 示例**<br>
> >   1、DNS-over-HTTPS（DoH）
> >   ```ruby
> >   dns-server = https://dns.alidns.com/dns-query
> >   ```
> >   2、DNS-over-HTTP/3（DoH3）
> >   ```ruby
> >   dns-server = h3://dns.alidns.com/dns-query
> >   ```
> >   3、DNS-over-QUIC（DoQ）
> >   ```ruby
> >   dns-server = quic://223.5.5.5
> >   ```
> >   4、DNS-over-TLS（DoT）
> >   ```ruby
> >   dns-server = tls://223.5.5.5
> >   ```
> 
> **备用DNS**
>   
> >   当覆写的 DNS 查询失败后回退备用 DNS 进行查询。如需指定多个 DNS，可用逗号分隔。`system` 表示回退到系统 DNS

### [DNS-over-PROXY](#使用目录)

> 通过代理转发 DNS 查询请求
>
> **proxy=name**
> 
> > 需要注意此处的代理名称仅支持 URL 编码<br>
> > 以 `香港 01` 示例：
> > ```ruby
> > dns-server=https://dns.google/dns-query#proxy=%E9%A6%99%E6%B8%AF%2001
> > ```
> 
> **ecs=子网范围**
> 
> > ecs 参数用于设置 EDNS Client Subnet (ECS)，向 DNS 服务器传递客户端的子网信息。ECS 允许 DNS 服务器根据指定的子网范围（而非实际客户端 IP）来返回最优结果
> 
> **ecs-override=true**
> 
> > ecs 参数的强制覆盖。即使客户端的实际 IP 提供了不同的地理位置，查询会强制使用 ecs 指定的子网范围
> > 
> > 示例：
> > ```ruby
> > dns-server=https://dns.google/dns-query#ecs=120.76.0.0/14|2620:149:af0::10/56&ecs-override=true
> > ```
> > ```ruby
> > dns-server=https://dns.google/dns-query#proxy=name&ecs=1.1.0.0/14|2620:149:af0::10/56&ecs-override=true
> > ```

### [no-resolve的作用](#使用目录)

> * 当域名请求遇到 IP 类规则时，Shadowrocket 会向本地DNS服务器发送查询请求，以判断主机 IP 是否匹配规则
> 
> * 若IP类规则加 `no-resolve`，则域名请求将会跳过此规则，不触发本地 DNS 查询。如：
>   ```ruby
>   IP-CIDR,172.16.0.0/12,DIRECT,no-resolve
>   ```

### [代理分组/策略组](#使用目录)

> * 点击配置文件的 `ⓘ` 图标 > 代理分组 > 右上角 `➕`。填写名称，根据需求选择类型，通过 `正则` 匹配策略，或者从策略输入框后面的 `•••` 手动添加策略，保存
> 
> * 策略是规则的组成部分，创建的代理分组只有放到规则里才能发挥作用
>   * 进入对应规则的详情页，点击策略选项，从列表中选择所需的代理分组，保存
> 
> * 首页下拉，可以快捷进入代理分组界面

### [代理分组类型](#使用目录)

> **select**：手动指定所用代理
> 
> **url-test**：根据设定的自动测试周期和结果自动切换延迟最低节点
> 
> **fallback**：节点不可用时自动切换其他可用节点，可用节点范围被上次自动测试结果所限
> 
> **load-balance**：不同规则的请求使用分组里的不同节点进行连接，相同的域名会使用同一个节点
> 
> **random**：随机使用分组里的不同节点进行连接，相同的域名可能使用不同的节点

### [脚本URL](#使用目录)

> 配置 > 配置文件 > 编辑配置 > 脚本 URL
> 
> 当前使用的所有远程脚本资源的展示页面，✅ 表示当前脚本状态生效，❎ 表示当前脚本状态失效，点击脚本地址可重新拉取并弹出状态提示，也可以点击 [使用配置](#使用配置)，对当前所有 URL 进行更新

### [规则集URL](#使用目录)

> 配置 > 配置文件 > 编辑配置 > 规则集URL
> 
> 当前使用的所有远程规则集资源的展示页面，✅ 表示当前规则集状态生效，❎ 表示当前规则集状态失效，点击规则集地址可重新拉取并弹出状态提示，也可以点击 [使用配置](#使用配置)，对当前所有 URL 进行更新

### [复制配置文件](#使用目录)

> 配置 > 点击配置文件 > 编辑配置 > 复制
> 
> 点击该选项可将当前配置生成一份备份并命名为 `*-copy.conf`

### [Hosts](#使用目录)

> **主要功能**
> > * 将特定域名映射到指定 IP 地址，绕过 DNS 解析，直接控制域名到 IP 的对应关系
> > * 将特定域名指定特定的 DNS 服务器进行解析
> 
> **常见用途**
> > * 屏蔽广告/追踪域名：将广告域名解析到无效 IP（如 0.0.0.0 或 127.0.0.1），使其无法加载
> > * 绕过 DNS 污染：强制将某些域名指向正确的 IP，避免被劫持
> > * 本地开发调试：将测试域名指向本地服务器 IP
> > * 加速访问：手动指定更快的 CDN IP

### [URL重写](#使用目录)

> **功能作用**
> > * 修改 HTTP(S) 请求/响应，动态拦截并修改请求的 URL、头部或内容
> 
> **常见用途**
> > * 去广告：将广告请求重定向到空地址或本地
> > * 反追踪：移除 URL 中的跟踪参数（如 utm_source）
> > * 路径修正：调整 API 请求路径以适配不同服务器
> > * 调试工具：将生产环境请求转发到测试服务器

### [HTTPS解密](#使用目录)

> 打开HTTPS解密方法：
> * 点击配置文件的 `ⓘ` 图标 > HTTPS 解密 > 证书 > 生成新的 CA 证书 > 安装证书
> 
> * 系统设置 > 已下载描述文件 > 安装
> 
> * 系统设置 > 通用 > 关于本机 > 证书信任设置 > 开启对应 Shadowrocket 证书信任

### [负载均衡](#使用目录)

> 使用负载均衡策略类型方法：
> 
> 点击配置文件的 `ⓘ` 图标 > 代理分组 > 右上角 `➕`，类型选择 `load-balance`
> 
> `load-balance` 表示不同规则的请求使用分组里的不同节点进行连接，相同的域名会使用同一个节点

### [模块](#使用目录)

> 模块是指为 Shadowrocket 提供额外功能的插件或者扩展项，一般是以增强或自定义软件的使用体验为出发点。模块的写法与配置文件相同，且模块的优先级高于配置文件，可以在模块里设置通用设置以及添加规则、Hosts、重写、脚本、证书内容、解密主机名等
>
> **下载远程模块**
> > * 配置 > 模块 > 右上角 `➕` > 填写链接 > 下载
> 
> **本地新建模块**
> > * 配置 > 模块 > 新建模块 > 编辑后保存
> > 
> >   模块 `[MITM]` 部分需要加 `%APPEND%`，表示把内容插入到配置中，不加时会覆盖配置中对应内容，并影响其他模块功能
> >   
> >   ```ruby
> >   hostname = %APPEND% 主机名
> >   ```
> 
> **备注**
> > * 对正在使用的配置 [开启 HTTPS 解密](#https解密)，才能使包含 MITM 的模块完整生效，不包含 MITM 的模块除外
> > * 因模块可能包含不同规则，所以大多数模块仅在 [全局路由](#全局路由区别) 设为配置时生效，不包含规则类的模块除外
> > * iOS 15 之后，NE的内存限制由 15 MB 增加到了 50 MB，低版本系统可能因内存不足导致 [模块失效](#模块失效) 或 [VPN 自动断开](#vpn自动断开)

### [证书模块](#使用目录)

> 切换配置文件时免除重复安装 CA 证书方法：
> 
> * 点击「已安装证书的配置文件」后面的 `ⓘ` 图标 > HTTPS 解密 > 证书后面的 `ⓘ` 图标 > 复制
> 
> * 新建模块：
> 
>   软件 `配置 > 模块 > 新建模块`，粘贴并自行修改以下内容：
>   
>   ```ruby
>   #!name=证书（名字可更改）
>   [MITM]
>   enable=true
>   ca-passphrase=证书密码（即「已安装证书的配置文件」的证书密码，默认密码是Shadowrocket）
>   ca-p12=证书内容（即剪贴板复制的内容）
>   ```
>   原本是可以省略 `ca-passphrase` 这行参数。但由于引用的配置文件可能已经包含了证书密码，且证书密码可能不是 Shadowrocket，为防止出错，因此才增加 `ca-passphrase` 参数来覆盖引用的配置文件的证书密码
> 
>   `enable=true` 忽略当前配置文件内的HTTPS解密状态，使用该模块的证书进行HTTPS解密

### [身份证书密码](#使用目录)

> Shadowrocket 安装 CA 证书时，如果遇到「输入证书 `身份证书` 的密码」页面，可以尝试输入：Shadowrocket

------

## [数据页面](#数据页面)

### [代理日志](#使用目录)

> `代理日志` 记录了网络活动过程中 Shadowrocket 处理请求的具体信息
> * 数据 > 代理 > 启用日志记录
> 
> * 产生网络活动时，返回 `数据 > 代理` 页面查看日志文件
> 
> * 每条记录包含信息：
>     * 请求 URL
>     * 请求匹配的规则策略
>     * 请求传输协议
>     * 请求发送时间
> 
> * 记录显示 `MITM`，表示请求域名已启用解密
> 
> * 点击每条记录查看详情，详情页右上角 `•••` 可以选择类型添加规则
> 
> * `数据 > 代理` 页面，右上角 `•••` 可以手动删除所有日志文件。日志文件页面，右上角 `•••` 可以选择导出
> 
>   `数据 > 自动删除 > 打开，程序会自动删除7天前的日志文件。Shadowrocket 已连接状态，手动删除将保留最新的日志文件，未连接时，手动删除所有`

### [DNS日志](#使用目录)

> `DNS 日志` 记录了网络活动过程中 DNS 服务器处理域名查询请求的具体信息
> * 数据 > 代理 > DNS > 启用日志记录
> 
> * 产生网络活动时，返回 `数据 > DNS` 页面查看日志文件
> 
> * 每条记录包含信息：
>     * 请求域名
>     * 查询结果
>     * DNS 响应时间
>     * 处理请求的 DNS
> 
> * 旗帜是根据返回IP地址的地理位置信息自动显示
> 
> * `覆写 DNS` 不可用或未返回有效响应时，将回退至 `备用 DNS` 来查询域名
> 
>   `记录信息中如果响应时间超过2秒，意味着系统正在触发回退机制`

### [iCloud自动同步](#使用目录)

> Shadowrocket 支持将服务器节点、配置文件、模块和脚本文件等数据类型自动同步至 iCloud 云端
> * 数据 > iCloud > 自动同步 > 打开
> 
> * 设备 `设置 > 账号 > iCloud`，确保使用iCloud的APP列表中已经开启 Shadowrocket 和 `iCloud云盘` 项目，否则会出现 `iCloud自动同步失败` 的提示
> 
> * 同步成功时，点击 `iCloud文件` 可以看到存储云端的配置文件
> 
> * `文件app > iCloud云盘 > Shadowrocket`，可以看到存储云端的所有数据。其中的 `shadowrocket.v2.model` 文件包含服务器节点的配置信息
> 
> * iCloud服务中断、网络连接问题以及其他复杂原因可能导致 iCloud 同步异常，这种情况建议选择手动删除iCloud备份并重新同步数据
> 
>   `如果用户删除首页某个节点后发现它又自动恢复，可以尝试以下解决方法：数据 > iCloud，服务器节点下面点击删除iCloud备份和同步服务器节点`
> 
> * 添加的 `场景` 和 `分组` 不属于 iCloud 自动同步的数据类型，需要手动备份下载，才能在设备间共享数据

### [节点数据管理](#使用目录)

> **导出节点**：将首页的所有节点数据整合成一个 JSON 文件，选择存储在本地或云端，也可以通过其他共享方式传输文件
> 
> **导入节点**：将存储在本地或云端 JSON 文件中的节点数据解析并添加到首页
> 
> **删除本地节点**：一键删除首页所有节点数据

### [流量统计信息](#使用目录)

> `统计` 是 Shadowrocket 开启连接后接管设备所有网络传输的流量统计信息
> * 数据 > 统计
> 
> * 统计包含信息：
>     * 开始时间
>     * 连接时间
>     * Wi-Fi 和蜂窝数据的上下行流量
>     * 流量分流的柱形图统计
> 
> * 默认记录所有流量统计信息。打开 `启用存档` 将会单独记录每一次连接的流量统计信息，关闭首页连接后可以从`归档`查看
> 
> * 点击右上角 `•••` 可以重置统计信息
> 
> 首页 `订阅` 支持显示流量统计信息。方法是在订阅链接指向的纯文本base64编码前添加 `STATUS=xxx` 或 `REMARKS=xxx` 字段，这样订阅名称下方就能显示自定义信息。如果没有添加字段或者隐藏用户代理字符串，可能导致不返回相关统计信息，只显示时间

------

## [设置页面](#设置页面)

### [延迟测试方法](#使用目录)

> 详见词条 [连通性测试](#连通性测试)

### [小组件](#使用目录)

> 设置 > 小组件
> > 
> > * **服务器节点**：根据需求添加6个常用节点，点击 `Today 小组件` 右上角的 `>` 可以展开查看，方便手动切换节点
> > 
> > * **显示Ping值**：启用后，长按 `Today小组件` 中心位置可以测试 `服务器节点` 连通性并显示延迟数字
> > 
> > * **根据Ping排序**：启用后，长按 `Today小组件` 中心位置可以测试 `服务器节点` 连通性并依延迟大小自动排序
> 
> 添加小组件方法：
> 
> Today 小组件
> 
> > * 负一屏 > 编辑 > 自定 > 点击 Shadowrocket 旁边的 `添加` 按钮  `➕`。（系统要求低于 iOS 18）
> 
> 屏幕小组件
> 
> > * 长按屏幕 > 左上角 `➕` > Shadowrocket，选择合适类型添加。（系统要求≥ iOS 17）
> 
> 更新 Shadowrocket 后，如果找不到小组件添加按钮，请尝试重启手机。如果小组件显示 `无法加载`，请尝试以下方法：
> 
> > * 系统设置 > 通用 > 语言与地区，添加或删除一种其他语言

### [按需求连接](#使用目录)

> **始终开启**
> > * VPN 保持连接状态。意外断开或者重启设备，也会自动连接
> > 
> > * `脚本 / 模块 / 解密` 等需求比较多时建议开启
> 
> **按需求连接**
> > * 根据添加的 `按需求规则` 自动切换 VPN 状态。默认规则是任意网络类型下保持连接状态，相当于 `始终开启`
> > 
> > * 按需求规则：
> >     * 当访问列表中的 `域名` 时，系统会向 Shadowrocket 发送请求，如果响应成功，VPN 自动连接
> >     * 网络中指定的 `DNS`（通常认为是网络运营商/Wi-Fi 路由器提供的 DNS 服务器地址）与列表任一内容相匹配时，VPN 自动连接或断开
> >     * `SSIDS` 填写需要匹配的 Wi-Fi 名称
> >     * VPN 连接行为可以通过 `网络类型 / 域名 / DNS` 条件触发
> >     * VPN 断开行为不能通过 `域名` 条件触发
> >     * 从上到下依次匹配添加的 `按需求规则`
> > * 添加 `按需求规则` 后，打开 `按需求连接` 开关，规则才能生效
> > 
> > * 同时打开 `始终开启` 和 `按需求连接`，只有 `始终开启` 选项能够生效
>   
> **睡眠时断开**
> > * 当设备进入睡眠状态，VPN 自动断开连接
> > 
> > * Shadowrocket 响应系统发送的睡眠指令才会断开连接，有时候熄屏的系统未必处于睡眠状态
> 
> **显示断开信息**
> > * 显示 VPN 断开连接的通知信息

### [隧道](#使用目录)

> **强制路由**
> 
> > 如果开启，这个隧道的路由规则将优先于任何本地自定义的路由，默认是关闭状态
> 
> **包括所有网络**
> 
> > 如果开启，所有网络流量都会通过隧道进行路由，但有以下排除项
> > 
> > * **包括本地网络**：如果开启，所有发送到本地网络的流量都将包含在隧道中
> > * **包括APNs**：如果开启，苹果的推送通知服务（APNs）的网络流量将包含在隧道中
> > * **包括蜂窝服务**：如果开启，来自蜂窝服务的互联网可路由网络流量（VoLTE、Wi-Fi通话、IMS、MMS、视觉语音信箱等）将包含在隧道中

### [前置代理](#使用目录)

> 设置 > 代理 > 前置代理
> 
> 「前置代理」表示所有流量先通过 HTTP/SOCKS5 代理转发，再根据配置规则向节点服务器发送请求

### [代理共享](#使用目录)

> 代理共享指的是将你当前配置的代理设置分享给其他设备使用。通过代理共享，你可以把自己配置好的代理服务器（如Shadowsocks、Vmess等）通过局域网或者热点网络的方式让其他设备也能够通过相同的代理设置访问互联网
> 
> **在局域网条件下**
> > * A设备：设置 > 代理 > 代理共享 > 启用共享
> > * B设备：系统设置 > WiFi > WiFi 名称后面的 `ⓘ` 图标 > HTTP代理 > 手动输入Shadowrocket「代理共享」的IP和端口
> 
> **使用热点条件下**
> > * A设备：开启热点
> > * B设备：连接热点
> > * 然后按照局域网条件下方法进行设置<br>
> >   `此处需要注意下操作顺序，原理是连接设备热点后先形成局域网环境，然后按照局域网条件进行设置`
> >
> **备注**
> > * 当 iOS 设备开启代理共享时，或需保持该设备屏幕常亮或连接充电器，以防意外退出
> > * 如果配置文件开启了 HTTPS 解密，请确保其他设备已安装并信任相同的证书才能正常使用。当其他设备不需要使用解密功能时，可以在“代理共享”页面关闭「HTTPS解密」开关
> > * 使用代理共享时需要对应的 APP 打开系统设置中的“本地网络”开关
> > * Telegram 可能不被系统代理接管，可单独在应用内添加 SOCKS5 代理


### [检测代理](#使用目录)

> 如果在使用 Shadowrocket 的时候，遇到某些 APP 提示需关闭代理才能使用，可以在 `Shadowrocket > 设置 > 代理类型 > 选择 None`

### [代理类型](#使用目录)

> Shadowrocket 代理类型：
> 
> * 设置 > 代理 > 代理类型
> 
> * **HTTP**：系统代理模式，对于不支持的程序会交给 tun 接管网络连接
> 
> * **None**：tun 模式，全部网络请求都将通过 tun 接口进行处理

### [开启UDP转发](#使用目录)

> * 设置 > UDP > 开启转发 > 打开
> 
> * 首页 > 订阅后面的 `ⓘ` 图标 > UDP转发 > 打开
> 
> * 首页 > 节点后面的 `ⓘ` 图标 > UDP转发 > 打开

### [隐藏VPN图标](#使用目录)

> 设置 > 排除路由 0.0.0.0/31 > 打开
> 
> **注意**：该选项其实是利用系统漏洞实现的，打开开关可能会导致网络异常。如遇问题，请关闭此项

### [GEOIP数据库](#使用目录)

> 设置 > GeoLite2 数据库
> 
> 方法一
> * 填写 [MaxMind官网](https://www.maxmind.com) 注册的账户 ID 和密钥，点击下方的 `更新` 按钮
> 
> 方法二
> * 关注 GitHub 的 IP 数据库项目，复制 mmdb 格式的下载链接，粘贴在国家/ASN 对应的 URL 位置，点击 `更新` 按钮。当点击 `重置` 时，可以恢复为系统自带的数据库
> 
>   [Loyalsoldier](https://github.com/Loyalsoldier/geoip) 的 IP 数据库：
>   ```ruby
>   https://raw.githubusercontent.com/Loyalsoldier/geoip/release/Country.mmdb
>   ```
>   [Hackl0us](https://github.com/Hackl0us/GeoIP2-CN) 的 IP 数据库：
>   ```ruby
>   https://github.com/Hackl0us/GeoIP2-CN/raw/release/Country.mmdb
>   ```
>   [Masaiki](https://github.com/Masaiki/GeoIP2-CN) 的 IP 数据库：
>   ```ruby
>   https://github.com/Masaiki/GeoIP2-CN/raw/release/Country.mmdb
>   ```
>   [P3TERX](https://github.com/P3TERX/GeoLite.mmdb) 的 ASN 数据库：
>   ```ruby
>   https://github.com/P3TERX/GeoLite.mmdb/raw/download/GeoLite2-ASN.mmdb
>   ```

### [自动更新](#使用目录)

> 现阶段软件的自动更新包含配置文件自动更新、服务器订阅自动更新以及 GeoLite2 数据库自动更新。需要在 `系统设置 > 通用 > 后台App刷新` 中为 Shadowrocket 启用后台刷新
> 
> * **配置**：自动 [更新配置](#更新配置) 功能。该功能可根据设置自动更新当前配置文件以及当前所用的规则集、脚本等远程资源。若当前配置文件使用的是从远程链接加载的，更新配置文件会使用原远程链接拉取全新配置替换当前配置，该操作会覆盖对该配置文件做过的所有自定义设置；若当前配置文件是默认配置或不含更新地址的配置文件，则自动更新功能仅会更新当前所用的规则集、脚本等远程资源
> 
>     * 自动后台更新：开启后可根据设置自动更新配置文件
>     * 更新提醒：开启后，更新时会弹出相应提醒。需要开启设备推送通知
>     * 更新间隔：单位为  `天`，可选 1-7 天
>     * 规则集/脚本资源手动更新方法：点击配置文件 > 使用配置
>     * 小技巧：若当前配置是远程配置，希望自动更新规则集等远程资源且不希望自定义设置被覆盖，可进入 [纯文本编辑](#编辑纯文本) 删除或注释掉 `update-url = *`
>   
> * **订阅**：[参见此处](#更新订阅节点)
> * **GeoLite2 数据库**：包含自动后台更新选项、更新提醒选项、更新间隔选项，其中更新间隔单位为 `天` 。其他设置 [参见此处](#GEOIP数据库)

### [温和策略机制](#使用目录)

> 当使用温和策略机制时，切换策略不会打断之前与之相关的TCP连接，仅会对之后的网络请求使用新的策略进行连接<br>
> 当不使用该功能机制时，切换策略会打断与该策略相关的旧有 TCP 连接，若继续使用则使用新的策略重新连接
> 
> 例如：打断会使旧有策略相关的连接所进行的下载任务中断

------

## [其他问题](#其他问题)

### [自动切换节点](#使用目录)

> 自动切换延迟低的节点：
> 
> **方法一**
> > * 首页 > 全局路由 > 分组 > 简单模式 > 打开
> 
> **方法二**
> > * 点击配置文件的 `ⓘ` 图标 > 代理分组 > 右上角 `➕` > 类型 `url-test`
> 
> **备注**
> > * 如果节点不稳定，可同时 [开启回退](#启用回退)

### [SSL错误](#使用目录)

> 添加/更新订阅链接时，如果提示 `发生了 SSL 错误，无法建立与该服务器的安全连接`，可以尝试的解决方法：
> 
> * 全局路由选代理，使用另外一个节点来添加/更新订阅链接
> 
> * 切换网络后再添加/更新订阅链接
> 
> * 检查订阅链接是否错误或失效

### [节点旗帜](#使用目录)

> 节点优先根据备注名称匹配旗帜，如果匹配不成功，由节点地址解析出 IP，通过数据库判断该IP的国家或地区，然后显示对应的旗帜
> 
> * 节点后面的 `ⓘ` 图标 > 地址栏的图标，可以手动修改旗帜
> * 订阅后面的 `ⓘ` 图标 > 订阅链接后面的 `ⓘ` 图标，利用脚本也能批量修改旗帜
> 
> 如果把旗帜的 Emoji 放在节点备注开头，保存时会自动显示对应的旗帜

### [节点感叹号](#使用目录)

> 节点显示感叹号原因：
> 
> * 您的节点使用了 TLS，地址是 IP，却没有设 SNI
> 
> 这不是正确的服务器设置，但为了可以正常连接，Shadowrocket 会主动开启 `允许不安全`。`允许不安全` 将跳过TLS证书验证，这将导致一些安全问题。如果您使用自签名证书，请将证书导入系统并信任它，否则请及时续订服务器端证书，以防止证书过期。在 `2.2.23` 等特定版本中，该选项可能默认为关闭状态

### [微信转圈](#使用目录)

> 如果使用 Shadowrocket 时微信一直显示 `连接中/收取中`，可以尝试的解决方法：
> 
> * 微信分流走直连
> 
> * 点击配置文件的 `ⓘ` 图标 > 通用 > 启用IPv6 > 关闭
>   
> 本质上该问题是由于使用的分流对 IPv6 分流不恰当，可能造成国内的部分 IPv6 地址被错误地分流至代理隧道造成的

### [模块消失](#使用目录)

> 模块页面已经开启 `保存到iCloud`，如果出现模块消失的问题，请检查：
> 
> * 系统设置 > Apple ID > iCloud > 使用iCloud的APP中，确保Shadowrocket/iCloud云盘已经打开同步
> 
> * 文件app > iCloud云盘 > Shadowrocket，确定其中包含 `Modules` 和 `Script` 两个子文件夹
> 
> * 文件app > iCloud云盘 > Shadowrocket > Modules，如果iCloud的本地缓存被清理，此时模块文件是未下载状态，请等待自动下载或手动下载

### [模块失效](#使用目录)

> 加载资源时可能因为内存、网络等原因导致出现部分内容漏编译的情况。尝试对当前配置点击“使用配置”，以使远程资源进行重新拉取，一般可恢复正常
> 
> 前提是模块确认有效，解密设置无误

### [VPN自动断开](#使用目录)

> 系统版本低于 `iOS 15` 处理复杂请求、加解密数据、运行脚本等因素相互作用之下可能导致 NE 内存占用过高，从而造成 VPN 自动断开，解决方法：
> 
> `设置 > 按需求连接 > 始终开启 > 启用`

### [定位权限](#使用目录)

> * iOS 系统的要求，开启定位权限才能获取 Wi-Fi 名称
> 
> * 如果不需要在 Shadowrocket 里看到 Wi-Fi 信息，那么就可以不用开启

### [编译原因](#使用目录)

> Shadowrocket 2.2.29 之前的版本是使用 Xcode 13.2.1 编译的
> 
> 2023年4月份以后，苹果官方要求开发者在提交应用到 App Store 时必须至少使用 Xcode 14 编译，所以 iOS12 以下系统无法使用
> 
> Shadowrocket 在版本 `2.2.30` 之后设置最低安装要求 iOS12，然后停止 `2.2.29` 版本，iOS 低版本用户可以安装 `2.2.28` 版本

### [下载Shadowrocket](#使用目录)

> Shadowrocket 只有 `iOS / iPadOS / tvOS` 版本和 M 系列芯片的 Mac 才能下载，开发者是 `Shadow Launch Technology Limited`。**Shadowrocket没有 安卓 / Windows 版本！**
> 
> 下载方法：
> * 非国区 ID 登陆 App Store，搜索 Shadowrocket，购买后下载<br>
> * Shadowrocket 是买断制的付费软件<br>
> * 美区价格：2.99 美元<br>
> * 使用美区 ID 时，地址建议填免税州
>   ```ruby
>   五个免税州：
>   俄勒冈州（Oregon）
>   蒙大拿州（Montana）
>   特拉华州（Delaware）
>   新罕布什尔州（New Hampshire）
>   阿拉斯加州（Alaska）部分区域
>   ```
> 
> [美国地址生成器](https://www.meiguodizhi.com)<br>
> [美区 Apple ID 注册方法](https://blog.skylershu.com/post/apple-id-us-2022)<br>
> [Apple 官网购买礼品卡方法](https://blog.skylershu.com/post/apple-gift-card)<br>
> [Shadowrocket 下载链接](https://apps.apple.com/app/shadowrocket/id932747118)

### [URL-Schemes](#使用目录)

请使用相应内容直接替换代码中的大括号及其内容

> `启动 VPN 隧道` 
> ```ruby
> shadowrocket://connect
> ```
> ```ruby
> shadowrocket://open
> ```
>  `停止 VPN 隧道` 
> ```ruby
> shadowrocket://disconnect
> ```
> ```ruby
> shadowrocket://close
> ```
>  `切换 VPN 开关状态` 
> ```ruby
> shadowrocket://toggle
> ```
>  `使用特定节点` 
> ```ruby
> shadowrocket://select?s={节点名称}
> ```
>  `添加 订阅/节点` 
> ```ruby
> shadowrocket://add/{url}
> ```
>  `安装/使用 配置` 
> ```ruby
> shadowrocket://config/add/{url}
> ```
>  `安装/使用 模块` 
> ```ruby
> shadowrocket://install?module={url}
> ```
>  `切换全局路由（代理/配置/直连/场景）` 
> ```ruby
> shadowrocket://route/proxy
> ```
> ```ruby
> shadowrocket://route/config
> ```
> ```ruby
> shadowrocket://route/direct
> ```
> ```ruby
> shadowrocket://route/scene
> ```
> `安装/使用 配色` 
> ```ruby
> shadowrocket://color?{配色设置}
> ```

------
