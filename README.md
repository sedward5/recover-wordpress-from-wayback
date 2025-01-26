# Hugo Static Site Automation Scripts

This repository contains scripts to assist with migrating and managing a static website built using Hugo. These tools streamline the process of recovering content, optimizing images, and maintaining a clean and efficient repository.

---

## **Table of Contents**
1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Scripts](#scripts)
   - [Wayback Machine Content Recovery](#1-wayback-machine-content-recovery)
   - [Image Downloader](#2-image-downloader)
   - [Image Optimization and Conversion](#3-image-optimization-and-conversion)
   - [Markdown Image Path Update](#4-markdown-image-path-update)
   - [Remove Redundant Images](#5-remove-redundant-images)
4. [Usage](#usage)
5. [License](#license)

---

## **Overview**

The scripts in this repository are designed to:
1. Recover content from the Internet Archive's Wayback Machine.
2. Download and optimize images from a CDN.
3. Convert images to WebP format and resize them based on use (e.g., featured images or inline images).
4. Update image references in Hugo Markdown files.
5. Remove redundant image files after conversion.

---

## **Prerequisites**

- Python 3.8+ installed
- Required Python libraries:
  - `Pillow`
  - `Requests`
  - `BeautifulSoup4`

Install dependencies using:
```bash
pip install -r requirements.txt
