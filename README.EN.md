# Cursor Pro Automation Tool User Guide

README also available in: [中文](./README.md), [Tiếng Việt](./README.VI.md)

## Features
Automatic account registration, automatic token refresh, hands-free operation.

## Download
[https://github.com/chendeben/cursor-auto-free/releases](https://github.com/chendeben/cursor-auto-free/releases)

## Important Notes
1. **Please ensure Chrome browser is installed. If not, [click here to download](https://www.google.com/chrome/)**
2. **Account login is required, regardless of whether the account is valid or not**
3. **Stable network connection is needed, preferably using foreign servers. Do not enable global proxy**

## How to Run

### Mac Version
1. Open terminal and navigate to the application directory
2. Run command to make the file executable:
```bash
chmod +x ./CursorPro
```
3. Run the program:
   - In terminal:
```bash
./CursorPro
```
   - Or double-click in Finder


Note: If you encounter the following issue; [Solution](https://sysin.org/blog/macos-if-crashes-when-opening/)


![image](./screen/c29ea438-ee74-4ba1-bbf6-25e622cdfad5.png)


### Windows Version
Simply double-click `CursorPro.exe` to run


## How to Verify if it Works
**After running the script, restart your editor. You'll know it's working when the account shown in the image below matches the account in your script's output log.**
![image](./screen/截屏2025-01-04%2009.44.48.png)


This project is modified from [gpt-cursor-auto](https://github.com/chengazhen/cursor-auto-free). The email retrieval part has been modified with a built-in email system API, eliminating the need for email configuration and automatically using temporary emails for verification codes.

## Update Log
- **2025-01-21**: Removed  configuration requirement
