# جادو (Jadu)

مجموعه‌ای از workflowهای آماده برای agentهای هوش مصنوعی، مخصوص جلسات کاری ساختارمند و پربازده. ریپو را فورک کنید، workflowهای موردنیاز را در پروژه‌تان کپی کنید، و از آن‌ها در Claude Code یا Codex استفاده کنید.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## workflowهای موجود

| workflow | Claude Code | Codex | کارایی |
|---|---|---|---|
| Bidar | `/jadu-bidar` | skill `jadu-bidar` | شروع جلسه — وضعیت پروژه را می‌خواند، زیروظایف برنامه‌ریزی را کامل‌تر می‌کند، و یادآور تمرکز ۳۰ دقیقه‌ای را تنظیم یا پیشنهاد می‌کند |
| Zad | `/jadu-zad` | skill `jadu-zad` | ویزارد راه‌اندازی پروژه — سوالات را یک‌جا می‌پرسد و فایل‌های context پروژه را می‌سازد |
| Kar | `/jadu-kar` | skill `jadu-kar` | مدیریت وظایف از طریق مکالمه در `TASKS.md` |
| Payan | `/jadu-payan` | skill `jadu-payan` | پایان جلسه — خلاصه فشرده می‌نویسد و مستندات/وظایف را بر اساس آن به‌روزرسانی می‌کند |
| Push | `/jadu-push` | skill `jadu-push` | stage، commit و push فقط وقتی کاربر صریحاً درخواست کند |

`jadu-tamam` به `jadu-payan` تغییر نام داده است.

---

## نحوه استفاده

### Claude Code

دستورهای موردنیاز را در دایرکتوری `.claude/commands/` پروژه‌تان کپی کنید:

```bash
cp .claude/commands/jadu-bidar.md /your-project/.claude/commands/
```

یا همه دستورهای Claude Code را به‌صورت سراسری نصب کنید:

```bash
mkdir -p ~/.claude/commands
cp .claude/commands/jadu-*.md ~/.claude/commands/
```

### Codex

فولدرهای skill موردنیاز را در پروژه یا مسیر skillهای Codex کپی کنید:

```bash
mkdir -p ~/.codex/skills
cp -R .codex/skills/jadu-* ~/.codex/skills/
```

سپس یک جلسه جدید Codex باز کنید و workflow را با نامش صدا بزنید؛ مثلاً `jadu-bidar`.

### راهنمای مشترک پروژه

برای پروژه‌هایی که چند agent دارند، فایل `AGENTS.md` را در ریشه پروژه نگه دارید. workflowهای Codex در جادو، `AGENTS.md` را منبع اصلی دستورالعمل‌ها می‌دانند. برای Claude Code می‌توانید یک `CLAUDE.md` کوچک نگه دارید که به راهنمای مشترک اشاره کند.

---

## جریان پیشنهادی جلسه

1. `jadu-zad` — ساخت یا به‌روزرسانی فایل‌های context پروژه.
2. `jadu-bidar` — شروع جلسه، pull امن، خواندن context و انتخاب تمرکز.
3. `jadu-kar` — اضافه یا به‌روزرسانی وظایف.
4. `jadu-payan` — بستن جلسه و به‌روزرسانی مستندات.
5. `jadu-push` یا درخواست صریح `push` — commit و push فقط با درخواست واضح.

---

## سفارشی‌سازی

- **تغییر پیشوند** — پیشوند `jadu-` اختیاری است. فایل‌ها را به هر نامی که دوست دارید تغییر دهید (`/start`، `/push`، `/done`) و Claude Code نام‌های جدید را تشخیص خواهد داد.
- **ویرایش workflow** — هر دستور یا skill یک Markdown ساده است. مراحل، لحن، یا ساختار را متناسب با جریان کاری خود تغییر دهید.
- **هماهنگ نگه داشتن agentها** — اگر رفتار workflow تغییر کرد، هم `.claude/commands/` و هم `.codex/skills/` را به‌روزرسانی کنید.
- **اضافه کردن workflow جدید** — برای Claude Code یک فایل `.md` در `.claude/commands/` بسازید؛ برای Codex یک فولدر `.codex/skills/<name>/SKILL.md` بسازید.

---

## اختیاری: هشدار صوتی ۳۰ دقیقه‌ای

`jadu-bidar` فقط از یادآور ۳۰ دقیقه‌ای استفاده می‌کند. Claude Code اگر ابزار reminder داشته باشد می‌تواند آن را تنظیم کند. Codex ممکن است چنین ابزاری نداشته باشد؛ در این حالت skill فقط پیشنهاد می‌کند یک یادآور خارجی ۳۰ دقیقه‌ای تنظیم کنید.

برای Claude Code می‌توانید صدای اختیاری فعال کنید. به `ffplay` (بخشی از `ffmpeg`) و فایل `30.mp3` در مسیر `~/.claude/sounds/` نیاز است.

```bash
# نصب ffmpeg (اگر نصب نیست)
# macOS:  brew install ffmpeg
# Ubuntu: sudo apt install ffmpeg

# کپی فایل صوتی
mkdir -p ~/.claude/sounds
cp sounds/30.mp3 ~/.claude/sounds/
```

اگر فایل یا `ffplay` موجود نباشد، workflow بدون صدا ادامه می‌دهد.

---

## مشارکت

PR خوش‌آمد است. هنگام تغییر رفتار workflowها، دستورهای Claude Code، skillهای Codex و مستندات کاربر را هماهنگ نگه دارید.
