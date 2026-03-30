import fs from "fs";

const API_KEY = process.env.LANGBLY_KEY;

// 读取文件
let content = fs.readFileSync("README.md", "utf-8");

// === 1. 保护代码块 ===
const codeBlocks = [];
content = content.replace(/```[\s\S]*?```/g, (match) => {
  codeBlocks.push(match);
  return `__CODE_BLOCK_${codeBlocks.length - 1}__`;
});

// === 2. 术语保护 ===
const glossary = JSON.parse(fs.readFileSync("glossary.json", "utf-8"));

for (const [key, value] of Object.entries(glossary)) {
  const regex = new RegExp(key, "g");
  content = content.replace(regex, `__TERM_${key}__`);
}

// === 3. 调用翻译 API ===
const res = await fetch("https://api.langbly.com/language/translate/v2", {
  method: "POST",
  headers: {
    "Authorization": `Bearer ${API_KEY}`,
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    q: content,
    source: "zh",
    target: "en"
  })
});

const data = await res.json();
let translated = data.data.translations[0].translatedText;

// === 4. 还原术语 ===
for (const [key, value] of Object.entries(glossary)) {
  const regex = new RegExp(`__TERM_${key}__`, "g");
  translated = translated.replace(regex, value);
}

// === 5. 还原代码块 ===
translated = translated.replace(/__CODE_BLOCK_(\d+)__/g, (_, i) => {
  return codeBlocks[i];
});

// === 6. 写入文件 ===
fs.writeFileSync("README.en.md", translated);

console.log("✅ Translation complete");
