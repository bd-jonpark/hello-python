# hello-python

A simple Python project with intentional defects for testing Coverity static analysis.

## Included Defects

| Defect Type | Description |
|-------------|-------------|
| SQLI | SQL injection vulnerability |
| COMMAND_INJECTION | Command injection via os.system |
| PATH_TRAVERSAL | Path traversal vulnerability |
| HARDCODED_CREDENTIALS | Hardcoded passwords |
| INSECURE_DESERIALIZATION | Unsafe pickle.loads |
| RESOURCE_LEAK | File handle not closed |
| NULL_RETURNS | None dereference |

## Run

```bash
python3 main.py
```

## Static Analysis

```bash
coverity scan --project-dir . --local ./output
```

## License

MIT
