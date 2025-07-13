---
layout: home
title: 🏠 Home
nav_exclude: false
nav_order: 1
---

# {{ site.tagline }}

{: .mb-2 }
{{ site.description }}
{: .fs-6 .fw-300 }

{{ site.staffersnobio }}

<!-- {: .warning }
This site is **under construction**. Anything you read here is not finalized. This disclaimer will be removed when the site is ready for Summer 2025. -->

<!-- {: .success }
>The Final Exam is **this Saturday, August 3rd from 11:30-2:30PM** in Mosaic 0204.
> 
> Our final review session will be held Friday, Aug 2nd, 12-2PM in HDSI 123 and at this [Zoom link](https://ucsd.zoom.us/j/91582761222?pwd=GkOIDavqvnTOb4Z5ixRQLNO1Z9hawe.1).
>
>If at least 75% of the class fills out both [SETs](https://academicaffairs.ucsd.edu/Modules/Evals/) and the internal [End-of-Quarter Survey](https://forms.gle/VKnJsw2JSHixkUDW6), then the entire class will have **1% of extra credit added to their overall grade**. The deadline is Saturday, August 3rd at 8AM. -->

<!--{: .success }
**Tip: When working on assignments, use Ctrl+F on this page to search for a keyword and quickly find the relevant lecture. Click the ✏️ emoji to open a static version of the lecture for reference, which is much faster than loading it on DataHub. Also, make sure to use the [reference sheet](https://drive.google.com/file/d/1ky0Np67HS2O4LO913P-ing97SJG0j27n/view?usp=sharing)!**-->

<!-- {: .success }
Welcome to DSC 10! To start, read the [syllabus](https://dsc10.com/syllabus) carefully, paying special attention to the ["Getting Started"](https://dsc10.com/syllabus/#-getting-started) section. Make sure to complete the Welcome Survey and [Pretest](https://practice.dsc10.com/pretest/) to get off to a good start! -->

<!-- {: .success}
We have a busy week in DSC 10. See [Ed](https://edstem.org/us/courses/60685/discussion/5101370) for a breakdown of the week's deadlines and our [recommended plan](https://edstem.org/us/courses/60685/discussion/5101370#:~:text=Weekly%20Plan%3A,DSC%2010%2Drelated%3A). -->

<!-- {: .success}
The Midterm Exam is this Thursday, July 18 from 11-11:50AM in Mosaic 0204, our usual lecture time and room. Details on logistics, format, etc can be found [on Ed](https://edstem.org/us/courses/60685/discussion/5105021). -->


[Jump to the current week](#week-3-simulation-sampling-confidence-intervals-midterm){: .btn }

{% for module in site.modules %}
{{ module }}
{% endfor %}
