# lee-kan.com — Lee & Kan Solicitors 改版提案

[Lee & Kan Solicitors](https://www.lee-kan.com/) 的網站改版：位於倫敦 Soho Lexington Street 的律師事務所，業務包括住宅及商業物業、公司商業、移民、遺囑遺產（Private Client）及訴訟。純靜態 HTML / CSS / JS，任何靜態主機都能直接部署。

> **概念設計展示**：這是由 [UX CIRCLES](https://ux-circles.com/web) 設計的改版提案，並非 Lee & Kan Solicitors 官方網站。
> 每頁頂端有「Concept」標示列，所有頁面都設為 `noindex`，`robots.txt` 也禁止搜尋引擎收錄，避免和官方網站搶搜尋結果。
> 如果律所正式採用：刪掉 `_build/build.py` 裡的 `.concept-bar` 和 `<meta name="robots" content="noindex, nofollow">`，重新建置，並把 `robots.txt` 改回 `Allow: /`。

## 頁面

| 頁面 | 內容 |
|---|---|
| `index.html` | 首頁：主視覺 + 聯絡卡（電話 / 電郵 / 地址）、六個業務範圍、四個工作承諾、常見收費、團隊、地圖與交通 |
| `services.html` | 六個業務範圍：簡介、服務清單、對應收費、「Ask about this」（自動帶入表單） |
| `fees.html` | 原本 17 頁 PDF 的收費資料整理成網頁：時薪、永久業權 / 租賃業權買賣、按揭、遺產承辦、移民收費表、追債，附側欄目錄 |
| `team.html` | 團隊五人 |
| `contact.html` | 諮詢表單（開啟預先填好的電郵，不需要後端）、聯絡方式、地圖 |

手機版底部固定「Call us / Get a quote」列。頁尾保留 SRA 數字徽章（Yoshki iframe，SRA 規定必須顯示），投訴、私隱、資料保護、多元統計的 PDF 連回官方網站。

## 原網站的主要問題

- 2015 年的模板，手機上無法正常瀏覽
- 收費資料只有一份 17 頁 PDF，首頁看不到任何價錢
- 電話號碼沒有可點擊連結，也沒有清楚的聯絡入口
- 團隊頁只有名字，服務頁只有一段文字

## 內容來源

所有文字、收費和團隊資料都取自官方網站及其 [LKPrices.pdf](https://www.lee-kan.com/LKPrices.pdf)。沒有加入律所未公布的資料（成立年份、律師簡歷、營業時間等）。移民收費中的 Home Office 費用以 PDF 所列日期為準（2023 年 10 月 / 2024 年 2 月），正式上線前需要律所確認是否已更新。

## 修改與建置

所有頁面由 `_build/build.py` 產生，頁首、頁尾、導覽列和聯絡資料只需改一處：

```
python3 _build/build.py
```

只需 Python 3。本機預覽：

```
python3 -m http.server 5180
```

然後打開 http://localhost:5180。

## 結構

```
index.html, services.html, fees.html, team.html, contact.html
assets/css/style.css
assets/js/main.js    手機選單、捲動效果、收費頁側欄定位、諮詢表單
assets/img/favicon.svg
_build/build.py      頁面產生器
```
