# Java Source Review Regex

**GOAL:** reduce a large Java codebase into a small high-signal set of files to review.

**FOCUS:** **entry points** → **data flow** → **dangerous sinks**

---

## Quick Workflow (Notepad++ / ripgrep)

1. Find **HTTP entry points**
2. Within those, find **user-controlled input**
3. Trace input to **DB/OS/file/deserialization sinks**
4. Check **reachability** (conditional logic, early returns)

Tip: prefer "few high-signal hits" over "thousands of results".

---

## 1) HTTP Entry Points (Servlets)

### Servlet handlers
- `doGet`, `doPost`, etc.
```regex
\bdo(Get|Post|Put|Delete|Options|Head|Trace)\s*\(
````

### Servlet classes

```regex
extends\s+HttpServlet\b
```

### Common frameworks (optional)

Spring MVC:

```regex
@\s*(RequestMapping|GetMapping|PostMapping|PutMapping|DeleteMapping|PatchMapping)\b
```

---

## 2) User-Controlled Input Sources

### Query/body parameters

```regex
\bgetParameter(s|Values)?\s*\(
```

### Headers / cookies / session

```regex
\bgetHeader(s)?\s*\(
\bgetCookies\s*\(
\bgetSession\s*\(
```

### Body / streams (raw input)

```regex
\bgetInputStream\s*\(
\bgetReader\s*\(
```

### URL path params (framework-dependent)

```regex
@PathParam\b
@RequestParam\b
@PathVariable\b
```

---

## 3) SQL / Database Sinks (SQLi Hunting)

### Direct query execution

```regex
\bexecute(Query|Update|Batch)\s*\(
```

### Statement creation

```regex
\bcreateStatement\s*\(
\bprepareStatement\s*\(
```

### “String-built SQL” patterns (high-signal)

SQL keyword + concatenation:

```regex
(?i)\b(select|insert|update|delete)\b.*\+
```

String literal containing SQL + concatenation:

```regex
(?i)".*\b(select|insert|update|delete)\b.*"\s*\+
```

String assignment with SQL (variable name agnostic):

```regex
(?i)\bString\s+\w+\s*=\s*".*\b(select|insert|update|delete)\b
```

### UNION / WHERE / ORDER BY helpers

```regex
(?i)\bunion\b
(?i)\bwhere\b
(?i)\border\s+by\b
```

---

## 4) OS Command Execution (RCE Sinks)

```regex
\bRuntime\.getRuntime\(\)\.exec\s*\(
\bProcessBuilder\s*\(
\bnew\s+ProcessBuilder\s*\(
```

---

## 5) File Read/Write (LFI/RFI-style impact, upload abuse)

```regex
\bFile(Input|Output)Stream\s*\(
\bFiles\.(read|write|newInputStream|newOutputStream)\s*\(
\bFileWriter\s*\(
\bBufferedWriter\s*\(
\bRandomAccessFile\s*\(
```

Uploads / multipart (useful for write primitives):

```regex
(?i)\bmultipart\b
(?i)\bFileItem\b
(?i)\bgetPart\s*\(
```

---

## 6) Deserialization (High-Risk)

```regex
\bObjectInputStream\s*\(
\breadObject\s*\(
\bXMLDecoder\s*\(
```

Common gadget surfaces / reflection:

```regex
\bClass\.forName\s*\(
\bgetMethod\s*\(
\binvoke\s*\(
```

---

## 7) SSRF / HTTP Client (pivoting)

```regex
\bHttpURLConnection\b
\bOkHttpClient\b
\bHttpClient\b
\bRestTemplate\b
\bURLConnection\b
```

---

## 8) XSS / SSTI-ish Sinks (context-dependent)

Output to response:

```regex
\bgetWriter\s*\(
\bprint(ln)?\s*\(
\bwrite\s*\(
```

Template / expression indicators:

```regex
\$\{
\#\{
```

---

## 9) Reachability / Guard Logic (to confirm exploitability)

Early exits:

```regex
\breturn\b
\bthrow\s+new\b
```

Null/empty checks (often bypassed by omitting params):

```regex
!=\s*null
==\s*null
!"?"?\.equals\(
\bStringUtils\.(isEmpty|isBlank)\b
```

Role/auth checks (decide if you need auth):

```regex
\b(isAdmin|isAuthenticated|hasRole|checkPermission)\b
\bAuthorization\b
\bJSESSIONID\b
```

---

## 10) Practical Triage Heuristics

High-signal combo to search in the *same file*:

* `doGet/doPost` **AND** `getParameter` **AND** (`executeQuery` OR SQL concat)
* `getParameter` **AND** `Runtime.exec` / `ProcessBuilder`
* `ObjectInputStream` / `readObject` anywhere
