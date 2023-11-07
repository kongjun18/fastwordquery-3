# Fast Word Query 3

Upgrade "Fast Word Query 2"  Anki add-on to Anki 23.10.

---

## Documentation

[User manual](https://ankiweb.net/shared/info/1807206748)

---

## Logs

Main menu -> `Tools` -> `Add-ons` -> `Fast Word Query 3` -> `View Files` -> `fastwordquery-3.log`.

---

## All versions

1. "Fast Word
   Query": [Add-on page](https://ankiweb.net/shared/info/1807206748), [GitHub](https://github.com/sth2018/FastWordQuery)
2. "Fast Word Query
   2": [Add-on page](https://ankiweb.net/shared/info/1501719123), [GitHub](https://github.com/aliahari/fastwordquery-2)
3. "Fast Word Query
   3": [Add-on page](https://ankiweb.net/shared/info/1956435337), [GitHub](https://github.com/Aleks-Ya/fastwordquery-3)

---

## Build ZIP

1. Run `gradlew`
2. Output is `build/fastwordquery-3.zip`

---

## Test cases for manual testing

### 1. Display "Options" window

1. Open Anki
2. Click "Tools" -> "FastWQ..."
3. Click "Dictionary Folder"
4. Click "Choose Note Type"
5. Click "Settings"
6. Click "About"
7. Click button with "gear" icon
8. Click button with "plus" icon

### 2. Fetching words from "Add note" window

1. Open "Add note" window
2. Enter word "desk"
3. Click "Query" -> "All Fields"
4. Clear retrieved fields
5. Press Ctrl-Q shortcut
6. Click "Query" -> "Options"

### 3. Fetching words from "Browser" window

1. Open "Browser" window
2. Select note for testing
3. Click "FastWQ" -> "Query Selected"
4. Click "FastWQ" -> "Options"
5. Click "FastWQ" -> "About"

### 4. Fetching words from context menu

1. Open "Browser" window
2. Select note for testing
3. RMB click in field -> "Query"

### 5. Config file

1. Start with absent config file
2. Start with existing config file
