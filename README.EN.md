[![Shadowrocket](https://socialify.git.ci/LOWERTOP/Shadowrocket/image?custom_description=User%20Manual&description=1&font=Rokkitt&forks=1&logo=https%3A%2F%2Fraw.githubusercontent.com%2FLOWERTOP%2FShadowrocket-First%2Frefs%2Fheads%2Fmain%2Fimg%2FShadowrocket.png&name=1&pattern=Plus&stargazers=1&theme=Light)](https://github.com/LOWERTOP/Shadowrocket "Repository URL")

[![README in Chinese](https://img.shields.io/static/v1?label=&message=README%20in%20Chinese&color=blue&logo=googletranslate&logoColor=white&labelColor=blue&messageColor=white)](https://lowertop.github.io/Shadowrocket "README in Chinese")

> [!NOTE]
> 
> The original repository for the Lazy Series config files and keyword list has become inactive. This repository will continue maintenance based on its final version or possible subsequent updates, with plans to refine the original keyword lists into a user manual for reference. The [Original branch](https://github.com/LOWERTOP/Shadowrocket/tree/Original) contains legacy files. The Lazy configurations provided by the [Johnshall repository](https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever) will also be updated based on this repository. For other needs, please visit the **[Themes & Configurations Repository](https://github.com/LOWERTOP/Shadowrocket-First)**. <br>
> We sincerely thank the original authors and all contributors to related projects!

------

# [Shadowrocket User Manual](https://lowertop.github.io/Shadowrocket/ "Release Page")

> [!NOTE]
> 
> **[Shadowrocket](https://apps.apple.com/us/app/shadowrocket/id932747118)** is a network proxy tool developed by **[Shadow Launch Technology Limited](https://shadowlaunch.com/)** specifically for iOS devices, also supporting Apple TV and Mac devices (M-series chips Only). Shadowrocket offers flexible configuration options, forwarding device network traffic through proxy servers to bypass specific network restrictions, access blocked content, enhance online privacy, and meet diverse user needs.

> [!TIP]
> 
> **Quick Start Guide**
> 
> > * Home > Add Node
> > * Settings > Latency Test Method > **`CONNECT`**
> > * Home > Connectivity Test, select an available node after testing
> 
> Upon first launch, you will be prompted to **`Install VPN Configuration Profile`**. Click **`Allow`** to proceed.

## [Table of Contents](#table-of-contents)
> [!TIP]
> * Click **section titles** to jump to related content.
> * Click **blue titles** in the body to return to the table of contents.

> * [Home Page](#home-page)
>     * [Add Node](#add-node)
>     * [Add WireGuard Node](#add-wireguard-node)
>     * [Update Subscription Nodes](#update-subscription-nodes)
>     * [Node Sorting](#node-sorting)
>     * [Node Sharing & Organization](#node-sharing--organization)
>     * [Subscription Node Filtering](#subscription-node-filtering)
>     * [Proxy Pass/Chain](#proxy-passproxy-chain)
>     * [Global Routing Differences](#global-routing-differences)
>     * [Connectivity Test](#connectivity-test)
>     * [Modify Test Address](#modify-test-address)
>     * [Scenarios](#scenarios)
>     * [Simple Mode](#simple-mode)
>     * [Enable Fallback](#enable-fallback)
> * [Config File](#config-page)
>     * [Config File](#config-file)
>     * [Use Config](#use-config)
>     * [Edit Config](#edit-config)
>     * [Edit Plain Text](#edit-plain-text)
>     * [Preview Config](#preview-config)
>     * [Update Config](#update-config)
>     * [Rename](#rename)
>     * [Export Config](#export-config)
>     * [Extend Config](#extend-config)
>     * [General Parameters](#general-parameters)💡
>     * [Add Rule](#add-rule)
>     * [Rule Priority](#rule-priority)
>     * [Rule Types](#rule-types)
>     * [Rule Policies](#rule-policies)
>     * [App Traffic Routing](#app-traffic-routing)
>     * [Update Rule Set](#update-rule-set)
>     * [Preview Rule Set](#preview-rule-set)
>     * [Modify DNS](#modify-dns)
>     * [DNS-over-PROXY](#dns-over-proxy)
>     * [Role of `no-resolve`](#role-of-no-resolve)
>     * [Proxy Group/Policy Group](#proxy-grouppolicy-group)
>     * [Proxy Group Types](#proxy-group-types)
>     * [Script URL](#script-url)
>     * [Rule Set URL](#rule-set-url)
>     * [Copy Config File](#copy-config-file)
>     * [Hosts](#hosts)
>     * [URL Rewrite](#url-rewrite)
>     * [HTTPS Decryption](#https-decryption)
>     * [Load Balancing](#load-balancing)
>     * [Modules](#modules)
>     * [Certificate Module](#certificate-module)
>     * [Identity Certificate Password](#identity-certificate-password)
> * [Data Page](#data-page)
>     * [Proxy Logs](#proxy-logs)
>     * [DNS Logs](#dns-logs)
>     * [iCloud Auto Sync](#icloud-auto-sync)
>     * [Node Data Management](#node-data-management)
>     * [Traffic Statistics](#traffic-statistics)
> * [Settings Page](#settings-page)
>     * [Latency Test Method](#latency-test-method)
>     * [Widgets](#widgets)
>     * [On-Demand Connection](#on-demand-connection)
>     * [Tunnel](#tunnel)
>     * [Upstream Proxy](#upstream-proxy)
>     * [Proxy Sharing](#proxy-sharing)
>     * [Proxy Detection](#proxy-detection)
>     * [Proxy Type](#proxy-type)
>     * [Enable UDP Forwarding](#enable-udp-forwarding)
>     * [Hide VPN Icon](#hide-vpn-icon)
>     * [GEOIP Database](#geoip-database)
>     * [Auto Update](#auto-update)
>     * [Graceful Policy Mechanism](#graceful-policy-mechanism)
> * [Other Issues](#other-issues)
>     * [Auto Switch Nodes](#auto-switch-nodes)
>     * [SSL Errors](#ssl-errors)
>     * [Node Flags](#node-flags)
>     * [Node Exclamation Mark](#node-exclamation-mark)
>     * [WeChat Loading Issue](#wechat-loading-issue)
>     * [Missing Modules](#missing-modules)
>     * [Module Failure](#module-failure)
>     * [VPN Auto Disconnect](#vpn-auto-disconnect)
>     * [Location Permission](#location-permission)
>     * [Compilation Reasons](#compilation-reasons)
>     * [Download Shadowrocket](#download-shadowrocket)
>     * [URL-Schemes](#url-schemes)

------

## [Home Page](#home-page)

### [Add Node](#table-of-contents)

> * Home > Top-left > Scan QR Code
>   
> * Copy node links (e.g., `trojan://*`, `vmess://*`, `vless://*`). Shadowrocket will auto-detect and import them when opened.  
>   `Requires clipboard access permission.`
> 
> * Home > Top-right `➕` > Type `Subscribe` > Enter subscription URL > Save.  
>   `Append "#1", "#2", "#3", etc., to reuse the same subscription.`
> 
> * Home > Top-right `➕` > Select node type > Fill in details > Save.  
>   **Supported protocols**: `Shadowsocks, ShadowsocksR, Subscribe, Vmess, VLESS, Relay, Socks5, Socks5 Over TLS, HTTP, HTTPS, HTTP2, Trojan, Hysteria, Hysteria2, TUIC, Juicity, WireGuard, Snell v2, Brook, Lua`.

### [Add WireGuard Node](#table-of-contents)

> * Home > Top-right `➕` > Select `WireGuard` > Fill in details.
> 
> * Copy WireGuard config in the following format. Shadowrocket will auto-detect and prompt for addition:
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
>   If not prompted, enable `Detect Clipboard` in settings or manually paste via `Paste` under the Connectivity Test.

### [Update Subscription Nodes](#table-of-contents)

> * Swipe left on subscription > Update.
> * Click refresh button 🔄 on Home.
> * Settings > Subscription > Update on Launch (reopen app).
> * Settings > Subscription > Auto Background Update (enable in `Settings > General > Background App Refresh`).
> * Use Shortcuts for automation.
> * Long-press app icon > Update Subscription.
> 
> **Common errors**:
> * **Forbidden**: Subscription reset or token error.
> * **Not Found**: Incorrect path.
> * **Service Unavailable**: Domain blocked or incorrect.

### [Node Sorting](#table-of-contents)

> Settings > Subscription > Sort by `Ping`.

### [Node Sharing & Organization](#table-of-contents)

> **Sharing**:
> > * Long-press node > Copy to share.
> > * Swipe left on node > QR Code. Other devices can scan to add.  
> >   `Note: QR standards vary. Some Vmess nodes may lose info when scanned by other tools.`
> > * Tap node’s `ⓘ` > Share options.
> > * Edit mode (`•••`) > Select nodes > Copy multiple links.
> 
> **Organization**:
> > * Reorder subscriptions via drag (`≡` icon).
> > * Group local nodes via `Fold` in edit mode.
> > * Delete nodes via edit mode > Delete.
> > * Swipe nodes for Test/Copy options.

### [Subscription Node Filtering](#table-of-contents)

> **Filtering**:
> > * Home > Subscription’s `ⓘ` > Filter.
> > * Regex examples:
> >   ```ruby
> >   /(?=.*(A))^(?=.*(B))^.*$/  # Retain nodes with A and B
> >   A|B                        # Retain nodes with A or B
> >   /^((?!(A|B)).)*$/          # Exclude nodes with A or B
> >   /(?=.*(A))^((?!(B)).)*$/   # Retain A, exclude B
> >   ```
> 
> **Batch Processing**:
> > * Rename nodes:
> >   ```ruby
> >   $server.title=$server.title.replace(/KeywordA/g,'KeywordB')
> >   ```
> > * Enable features:
> >   ```ruby
> >   $server.mux=1  # Enable multiplexing
> >   ```
> > * Proxy chain setup:
> >   ```ruby
> >   $server.chain="Subscription/Node"
> >   ```

### [Proxy Pass/Chain](#table-of-contents)

> Chain proxies through multiple nodes:
> * Select Node A > `ⓘ` > Proxy Pass > Choose Node B. Traffic path: `Client > B > A > Server`.
> * Use entire subscription as chain (random node selection).
> * Cancel via `ⓘ` > Proxy Pass > Remove.

### [Global Routing Differences](#table-of-contents)

> * **Config**: Traffic routed per rules.
> * **Proxy**: All traffic via one node.
> * **Direct**: No proxy.
> * **Scenario**: Auto-switch routing based on network type (Wi-Fi/Cellular).

### [Connectivity Test](#table-of-contents)

> Home > Connectivity Test. Delays shown in ms.  
> **Methods** (Settings > Latency Test Method):
> * **TCP**: TCP handshake time.
> * **ICMP**: Ping time.
> * **CONNECT**: HTTP HEAD request (recommended).  
> Use <https://www.speedtest.net> for speed tests.

### [Modify Test Address](#table-of-contents)

> **For Home/Group Tests**:
> > * Settings > Latency Test Method > URL Settings.
> > * Home > Test URL icon > URL Settings.
> 
> **For Proxy Group Tests**:
> > * Config > `ⓘ` > Proxy Group > Edit > URL field.

### [Scenarios](#table-of-contents)

> Auto-switch routing based on network type:
> * Home > Global Routing > Scenarios > Add.
> * Set rules per Wi-Fi/SSID or Cellular interface (e.g., `pdp_ip0`).
> * Location permission required for SSID detection.

### [Simple Mode](#table-of-contents)

> Auto-switch to low-latency nodes:
> * Home > Global Routing > Group > Simple Mode.
> * Test interval: 600s (default). Tolerance: 0ms (strict switching).
> * Affects `proxy` policy rules. Works even when Global Routing is set to Proxy.

### [Enable Fallback](#table-of-contents)

> Home > Global Routing > Enable Fallback.  
> Switches nodes after 3 failures. Random selection. Check [Proxy Logs](#proxy-logs) for details.

------

## [Config Page](#config-page)

### [Config File](#table-of-contents)

> Shadowrocket config files (`.conf`) simplify setup. Built-in `default.conf` covers basic rules.  
> **Add Config**:
> > * From URL: Config > `➕` > Paste link > Download > Use.
> > * From local/cloud: Config > Import.
> 
> **Actions**:
> > * Use Config, Edit, Edit Plain Text, Preview, Update, Extend, Rename, Export.

### [Use Config](#table-of-contents)

> Activate config and update remote resources (rule sets, scripts).

### [Edit Config](#table-of-contents)

> Adjust settings via UI. Some options require [plain text editing](#edit-plain-text).

### [Edit Plain Text](#table-of-contents)

> Directly edit config text. Reference examples:
> > * [Lazy Config](https://raw.githubusercontent.com/LOWERTOP/Shadowrocket/main/lazy.conf)
> > * [Lazy Config with Groups](https://raw.githubusercontent.com/LOWERTOP/Shadowrocket/main/lazy_group.conf)

### [Preview Config](#table-of-contents)

> View raw text of remote configs.

### [Update Config](#table-of-contents)

> Pull updates for remote configs. Enable auto-update in settings.

### [Rename](#table-of-contents)

> Rename the config file.

### [Export Config](#table-of-contents)

> Export as file.

### [Extend Config](#table-of-contents)

> Inherit settings from another config. Modify via `ⓘ` > General > Include Config.

### [General Parameters](#table-of-contents)

> Key parameters (💡 = text-only):
> * **bypass-system**: Disabling may cause system issues.
> * **dns-server**: Override DNS (e.g., `https://dns.alidns.com/dns-query`).
> * **ipv6**: Enable/disable IPv6 support.
> * **hijack-dns**: Redirect hardcoded DNS queries.
> * **stun-response-ip**: Mask real IP for WebRTC.
> * **compatibility-mode**: TUN/proxy behavior.

### [Add Rule](#table-of-contents)

> Define traffic routing rules. Match order: top-down, domain > IP.  
> Use Proxy Logs to capture and add rules.

### [Rule Priority](#table-of-contents)

> Higher rules take precedence. Domain rules > IP rules. Module rules > config rules.

### [Rule Types](#table-of-contents)

> **DOMAIN-SUFFIX**: Match domain suffix.  
> **DOMAIN-KEYWORD**: Match keyword in domain.  
> **IP-CIDR**: Match IP range. Add `no-resolve` to skip DNS.  
> **GEOIP**: Geo-based IP matching.  
> **FINAL**: Fallback policy.

### [Rule Policies](#table-of-contents)

> **PROXY**, **DIRECT**, **REJECT** variants. Can also target proxy groups.

### [App Traffic Routing](#table-of-contents)

> Route specific apps via rules. Example for YouTube:
> ```ruby
> RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/YouTube/YouTube.list,PROXY
> ```

### [Update Rule Set](#table-of-contents)

> Manually: Use Config. Automatically: [Auto Update](#auto-update).

### [Preview Rule Set](#table-of-contents)

> Swipe left on rule set > Preview.

### [Modify DNS](#table-of-contents)

> **Override DNS**:
> ```ruby
> dns-server = 1.1.1.1, tls://dns.google
> ```
> **Fallback DNS**:
> ```ruby
> fallback-dns-server = system
> ```

### [DNS-over-PROXY](#table-of-contents)

> Route DNS via proxy:
> ```ruby
> dns-server=https://dns.google/dns-query#proxy=NodeName&ecs=1.1.0.0/14
> ```

### [Role of `no-resolve`](#table-of-contents)

> Skip DNS resolution for IP rules. Example:
> ```ruby
> IP-CIDR,172.16.0.0/12,DIRECT,no-resolve
> ```

### [Proxy Group/Policy Group](#table-of-contents)

> Create groups (select, url-test
