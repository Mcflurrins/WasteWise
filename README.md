# Human-Computer Interaction Final Project: Prototype Design and Research Project

<https://canvas.anu.edu.au/courses/2781/assignments/11552>

This repository is to submit Final Project: Prototype Design and Research Project from Human-Computer Interaction, COMP3900/6390.

If you're a student in this class, there are a few things you need to do to get started.

## To start

1. fork this project to your own "uid" [GitLab](https://gitlab.cecs.anu.edu.au/)
   account

2. when you fork it, make sure that you don't change the name

3. when you fork it, make sure that the visibility level of the project remains "private", our marker user is added automatically.

## For the assignment

1. Read the assignment specification carefully on Canvas.

2. Follow appropriate data gathering and analysis processes to address the research challenge.

3. Upload research data and analysis scripts as well as other relevant files in the `materials` directory of your fork of this template repository.

4. Write your study documentation following the template in the repository. Use proper markdown syntax to format your document and display images.

5. Don’t forget to include at least two references to external sources in ACM format in your documentation.

6. commit and **push** your changes to GitLab

7. wait for the CI/CD jobs to complete (click CI/CD and then Jobs in the left sidebar), you should see all green ticks.

_Note_: you can push as many times as you like and all versions are backed up on GitLab with the time and date that you pushed it. Push early and push often.

## Help with Gitlab and Markdown

If you are having trouble with Gitlab or Markdown, we have some resources on this page: <https://canvas.anu.edu.au/courses/2781/pages/help-with-gitlab-and-markdown>

You can also go straight to the course forum and ask questions at any time for help with these technologies.

The short version is:

- **Gitlab:** have a look at this page <https://comp.anu.edu.au/docs/gitlab/>
- **Markdown:** read this website <https://www.markdownguide.org>

**Markdown Formatting Check:** There is a CI/CD job that checks your markdown formatting using the [`markdownlint-cli`](https://github.com/igorshubovych/markdownlint-cli) tool. Syntax rules are listed [here](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md) in our script, rules `MD013` and `MD041` are disabled. All other rules are active.

## Getting help

If you have any questions or problems, ask in consultation time after your tutorial or on the course forum.

## Note on PDF generation

This repository automatically generates PDF files from markdown files to create the a nice version of your assessment documents.

This is controlled by scripts in the `.gitlab-ci.yml` file. 

Sometimes this process doesn't work the way you might expect so if you notice something wrong or unexpected in the artefact PDF, ask on the course forum.

In particular, due to how the Pandoc tool generates a PDF (using LaTeX), images float to where they fit in the document. If you have a lot of images in one place, they may float to the end of the document. This behaviour is acceptable but you should make sure that you refer to your images in your text (E.g., "The distribution of responses to the SUS survey is shown in Figure 1").

