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
```

## **Scripts**

### **1. Wayback Machine Content Recovery**
- **Description:** Fetches blog content from the Wayback Machine and saves it to the `content/` directory in Hugo-compatible Markdown or HTML format.
- **Usage:**
  ```bash
  python wayback_recovery.py
  ```

---

### **2. Image Downloader**
- **Description:** Downloads images from a CDN or Wayback Machine based on references in Markdown files, storing them locally in the appropriate content directory.
- **Usage:**
  ```bash
  python image_downloader.py
  ```

---

### **3. Image Optimization and Conversion**
- **Description:** Converts JPEG and PNG images to WebP format and resizes them based on use:
  - Featured images (`featured_`) are resized to a maximum width of 1920px.
  - Inline images are resized to a maximum width of 800px.
- **Usage:**
  ```bash
  python image_optimization.py
  ```

---

### **4. Markdown Image Path Update**
- **Description:** Updates image references in Markdown front matter and body content to use the `.webp` extension after conversion.
- **Usage:**
  ```bash
  python update_image_paths.py
  ```

---

### **5. Remove Redundant Images**
- **Description:** Removes original JPEG and PNG files after confirming that WebP replacements exist and that Markdown files no longer reference the old file names.
- **Usage:**
  ```bash
  python remove_redundant_images.py
  ```

---

## **Usage**

1. **Recover Content:**
   Run the Wayback Machine Content Recovery script to fetch lost or archived content for your blog.

2. **Download Images:**
   Use the Image Downloader script to retrieve images from a CDN or the Wayback Machine.

3. **Optimize and Convert Images:**
   Execute the Image Optimization and Conversion script to create WebP versions of your images and resize them as needed.

4. **Update Markdown Files:**
   Update your Markdown files to reference the optimized WebP images using the Markdown Image Path Update script.

5. **Clean Up:**
   Remove redundant image files using the Remove Redundant Images script.

6. **Integrate with CI/CD:**
   Configure your GitHub Actions to run the Image Optimization and Markdown Update scripts on new commits to automate these processes.

---

## **License**

This repository is open source and available under the MIT License.
