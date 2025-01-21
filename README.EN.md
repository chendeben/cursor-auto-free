# Cursor Pro Automation Tool User Guide

## Features
Automatic account registration, automatic token refresh, hands-free operation.

## Download
[https://github.com/chendeben/cursor-auto-free/releases](https://github.com/chendeben/cursor-auto-free/releases)

## Important Notes
1. **Please ensure Chrome browser is installed. If not, [click here to download](https://www.google.com/chrome/)**
2. **Account login is required, regardless of whether the account is valid or not**
3. **Stable network connection is needed, preferably using foreign servers. Do not enable global proxy**

## Configuration Instructions
No configuration is required to use directly.
Download the `.env.example` file to the program's root directory and rename it to `.env`.

## Running Instructions
### Platform-specific Instructions
#### Environment Variables Configuration

You can configure the following options in the `.env` file:

```bash
# Optional Configuration
HEADLESS=true       # Enable headless mode (default: false)
PROXY='http://127.0.0.1:7890'  # Proxy server address (optional)
```

This project is modified from [gpt-cursor-auto](https://github.com/chengazhen/cursor-auto-free), with changes to the email retrieval part. It now has a built-in email system API, eliminating the need for email configuration, and automatically uses temporary email to receive verification codes.

## Update Log
- **2025-01-09**: Added logs and auto-build feature.  
- **2025-01-10**: Optimized email configuration.  
- **2025-01-11**: Added headless mode and proxy configuration through .env file.
- **2025-01-12**: Removed email configuration requirements.

Inspired by [gpt-cursor-auto](https://github.com/hmhm2022/gpt-cursor-auto).
