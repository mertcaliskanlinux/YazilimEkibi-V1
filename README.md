
# django-mdeditor


[![ENV](https://img.shields.io/badge/release-v0.1.20-blue.svg)](https://github.com/pylixm/django-mdeditor)
[![ENV](https://img.shields.io/badge/中文-v0.1.20-blue.svg)](./README_CN.md)
[![ENV](https://img.shields.io/badge/Gitter-v0.1.20-blue.svg)](https://gitter.im/django-mdeditor/Lobby)
[![ENV](https://img.shields.io/badge/python-2.x/3.x-green.svg)](https://github.com/pylixm/django-mdeditor)
[![ENV](https://img.shields.io/badge/django-1.7+-green.svg)](https://github.com/pylixm/django-mdeditor)
[![LICENSE](https://img.shields.io/badge/license-GPL3.0-green.svg)](https://github.com/pylixm/django-mdeditor/master/LICENSE.txt)

![](./django_and_editor.png)

**Django-mdeditor** is Markdown Editor plugin application for [django](djangoproject.com) base on [Editor.md](https://github.com/pandao/editor.md).

**Django-mdeditor** was inspired by great [django-ckeditor](https://github.com/django-ckeditor/django-ckeditor).

**Note:** 

- For Markdown page rendering issues, backend rendering is recommended. Because `Editor.md` has not been updated for a long time, some bugs and compatibility issues need to be debugged. Of course, front-end students can choose.
- Regarding the `Jquery` conflict, it cannot be deleted because it is required by the admin backend. It is recommended to separate the editing page on a single page or a full screen directly, using its own static file to distinguish it from other pages.

## Features

- Almost Editor.md features 
    - Support Standard Markdown / CommonMark and GFM (GitHub Flavored Markdown);
    - Full-featured: Real-time Preview, Image (cross-domain) upload, Preformatted text/Code blocks/Tables insert, Search replace, Themes, Multi-languages;
    - Markdown Extras : Support ToC (Table of Contents), Emoji;
    - Support TeX (LaTeX expressions, Based on KaTeX), Flowchart and Sequence Diagram of Markdown extended syntax;
- Can constom Editor.md toolbar 
- The MDTextField field is provided for the model and can be displayed directly in the django admin.
- The MDTextFormField is provided for the Form and ModelForm.
- The MDEditorWidget is provided for the Admin custom widget.

