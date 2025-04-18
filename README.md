# dev-tools

---

## 

Bundle multiple small utilities into one CLI:
- fakie
- hash string or file
- Timestamp converter
- JSON/YAML formatter
- MIME type detector
- decode jwt tokens (header + payload)
- check availability of local or remote port
- dns lookup
- encode/decode base64
- ip info
- http headers of a url
- who is lookup
- ping with color
- timezone converter
- license template
- inspect
  - Run introspection on Python objects or JSON blobs.
- serve
  - Start a simple HTTP server with CORS, custom dir, etc.
- csv2json / json2csv
  - Convert between CSV and JSON formats.
- difftext
  - Show a diff between two text inputs or files.
- iprange
  - Given CIDR or IP range, list all possible IPs.
- traceroute
  - Trace route to a host with color-coded hops (basic wrapper).
- remind
  - Set a CLI reminder that notifies after X time.
- timestamp diff
  - Compute duration between two timestamps.
- devtools uuid validate
  - Check if a given string is a valid UUID (v1–v5 support).
- devtools hexconvert
  - Convert between decimal, hex, binary, base64.
- devtools encoding
  - Detect and convert file encodings (UTF-8, Latin1, etc).
- table
  - Pretty-print data as a markdown table from CSV or JSON.
- filemeta
  - Output detailed file metadata: size, creation/mod time, permissions, mimetype.
  - Bonus: hash the file if --checksum is provided.
- headtail
  - Customizable head / tail tool with multi-file support and optional color coding.
- mkproject (pygen)
  - Scaffolds basic project structures for Python/Node/etc with templates.
- gitstats
  - Print Git repo stats: commits by author, commits/week, top changed files, etc.
- passcheck
  - Check password strength or test against HaveIBeenPwned API.
- regexdemo
  - Test regex interactively on text.
  - Bonus: highlight matches in terminal.
- cheatsheet
  - Local CLI-based reference for common tools (e.g., curl, jq, git).
- hash
  - Generate SHA1/SHA256/MD5 hashes of files or strings.
- sslcheck
  - Check the SSL/TLS certificate status of a domain (expiration date, issuer, and common name).
- depgraph
  - Generate dependency graphs for projects.
  - Scan a package file (like requirements.txt or package.json) and output a visual dependency tree (or DOT file) that you can further render.
- sysinfo
  - Print a summary of system hardware and OS info.
  - Report CPU details, memory usage, disk space, OS version, and network interfaces—helpful for diagnostics or reports.
- repohealth
  - Analyze repository health metrics.
  - Examine commit frequency, contributor activity, code churn, and even issue/PR stats. This can help teams get a quick dashboard of project activity.
- commitgraph
  - Generate an ASCII visualization of the Git commit graph (a lightweight alternative to full GUIs).
- sqlruncmd
  - Run and benchmark SQL queries against a SQLite database file, displaying execution times and results in a formatted table.
  - Example: devtools sqlruncmd --db mydb.sqlite "SELECT * FROM users LIMIT 10"
- commentfinder
  - Scan code files for special comments (e.g., TODO, FIXME, NOTE) and output a summary list with file names and line numbers for quick action.
- sphinx-doc
  - Generate Sphinx doc for a project
- unicodeinfo
  - Provide detailed information about Unicode characters—such as code point, name, and category—when given a character or string.






















