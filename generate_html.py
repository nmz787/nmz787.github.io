
import os
import time
import markdown
from lxml import etree as ElementTree

def get_head_and_body(nested_dir_level=0):
    relative_path_levels = ''.join(['../' for x in xrange(0, nested_dir_level)])
    head = """
    <!DOCTYPE html>
    <html class="fuelux" lang="en">
      <head>
        <meta charset="utf-8">
        <title>Nathan McCorkle</title>
        <!-- styles -->
        <link href="http://fuelcdn.com/fuelux/2.2/css/fuelux.css" rel="stylesheet" />
        <link href="http://fuelcdn.com/fuelux/2.2/css/fuelux-responsive.css" rel="stylesheet" />
        <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js" type="text/javascript"></script>
        <script src="http://fuelcdn.com/fuelux/2.2/loader.min.js" type="text/javascript"></script>
        <link href=\"""" + relative_path_levels + """css/docs.css" rel="stylesheet">
      </head>"""

    body_start = """
  <body data-spy="scroll" data-target=".subnav" data-offset="50">
    <div class="navbar navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </a>
          <a class="brand" href="http://nmz787.github.com">nmz787's blog</a>
          <div class="nav-collapse">
            <ul class="nav">          
              <li class="">
                <a href="http://nmz787.github.com"><i class="icon-home"></i> Home</a>
              </li>
              <li class="dropdown">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown"><i class="icon-comment"></i> Social <b class="caret"></b></a>
                <ul class="dropdown-menu">                                      
                    <li class=""><a href="http://www.twitter.com/norklemcdorkle" rel="tooltip" title="Go to twitter.com/nmz787" target="_blank">Twitter</a></li>
                    <li class=""><a href="http://github.com/nmz787" rel="tooltip" title="Go to github.com/nmz787" target="_blank">GitHub</a></li>
                    <li class=""><a href="http://www.linkedin.com/pub/nathan-mccorkle/9/98a/713" rel="tooltip" title="Go to LinkedIn profile" target="_blank">LinkedIn</a></li>
                </ul>
              </li>
              <li class="dropdown">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown"><i class="icon-list"></i> Projects <b class="caret"></b></a>
                    <ul class="dropdown-menu">
                        <li class=""><a href="https://github.com/nmz787/open-spectrometer" rel="tooltip" title="Go to open-spectrometer on GitHub" target="_blank">open-spectrometer</a></li>
                        <li class=""><a href="http://hackaday.io/project/1342-open-spectrometer" rel="tooltip" title="Go to open-spectrometer on hackaday.io" target="_blank">open-spectrometer (hackaday)</a></li>
                        <li class=""><a href="https://github.com/nmz787/rs232-sniffer" rel="tooltip" title="Go to rs232-sniffer on GitHub" target="_blank">rs232-sniffer</a></li>
                        <li class=""><a href="https://github.com/nmz787/microfluidic-cad" rel="tooltip" title="Go to microfluidic-cad on GitHub" target="_blank">microfluidic-cad</a></li>
                    </ul>
              </li>
              <li class="dropdown">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown"><i class="icon-list"></i> Code Snippets <b class="caret"></b></a>
                    <ul class="dropdown-menu">
                        <li class=""><a href="http://nmz787.github.com/fooplot.html" rel="tooltip" title="Go to fooplot">Fooplot test</a></li>
                        <li class=""><a href="https://gist.github.com/nmz787" rel="tooltip" title="GitHub short code snippets">My GitHub gists</a></li>
                        <li class=""><a href=\"""" + relative_path_levels + """html/about_this_blog.html" rel="tooltip" title="How and why this exists">About this blog</a></li>
                    </ul>
              </li>
            </ul>       
          </div>
        </div>
      </div>
    </div>"""
    return head + body_start

post_section_start = """
  <div class="container">
    <div class="marketing">
      <div class="content">   
        <div class="row">                           
          <div class="span7 columns">"""

def new_post_section(title, msg, link, img, date = time.strftime('%B %d, %Y')):
    mid2 = """
    <div class="row">
      <div class="span7">    
        <div class="row">
          <div class="span2">
            <a href="{0}" >
                <img border="0" width="250" height="250" src="{1}" alt="">
            </a>
          </div>
          <div class="span5">
            <h4><strong><a href="{0}">{2}</a></strong></h4>      
            <p>
              {3}
            </p>
            <p>
              <i class="icon-calendar"></i> {4}
            </p>
          </div>
        </div>
      </div>
    </div>
    """.format(link, img, title, msg, date)
    return mid2

post_section_end = """
         </div>
       </div>
    </div>
  </div>
</div>
"""

blog_start = """
    <div class="container"> 
      <div class="marketing">
        <div class="content">
          <!--div class="row"-->
            <!--div class="span9 column"-->
              <!--hr-->
            <!--/div-->
          <!--/div-->
          <div class="row">   
            <div class="span9 columns">
"""
blog_end = """
            </div>
          </div>
        </div>
      </div>
    </div>
"""

body_end = """
    <footer class="footer">
      <div>
        <p class="pull-right">  |  <a href="#">Back to top</a>  |       </p>        
        <p>Page last generated on """ + time.strftime('%B %d, %Y') + """</p>
        <p>If need be, <a href="https://github.com/nmz787/Feedback/issues/new" title="Leave feedback for Nathan"  target="_blank" >leave me some feedback</a>.</p>  
        <script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src="//platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script> 
      </div>
    </footer>
  </body>
</html>
"""

sections = {}

# walk the md directory to discover files
for root, dirs, files in os.walk(os.path.abspath('md')):
    # go through each file in the md directory
    for _file in files:
        with open(os.path.join(root, _file), 'r') as f:
            html = markdown.markdown(unicode(f.read(), 'utf-8'), output_format='xhtml5')
            html = '<div>{}</div>'.format(html)
            html_filename = os.path.splitext(_file)[0] + '.html'
            with open(os.path.join(os.path.abspath('html'), html_filename), 'w') as fh:
                s = (get_head_and_body(1) +
                     blog_start +
                     html +
                     blog_end +
                     body_end
                     )
                fh.write(s.encode('utf8'))

            # parse the markdown-cum-html, to get title, synopsis,
            # thumbnail image, and the date the page was last modified
            # all for adding an entry for the post to the index page
            elem = ElementTree.XML(html)
            title = elem.xpath('h1')[0].text
            msg = elem.xpath('p')[0].text
            msg = msg if len(msg)<=256 else msg[:256] + '...'
            img_elems = elem.xpath("//p/img[@title='blog_thumbnail']")
            img = img_elems[0].get('src') if len(img_elems) else ''
            img = (img if not img.startswith('../img') else img[len('../'):] ) if len(img) else 'img/blog_default.jpg'
            
            # get the time the .md file was last modified (or created)
            #date_created = os.path.getctime(os.path.join(root, _file))
            date_modified = os.path.getctime(os.path.join(root, _file))
            date = time.strftime('%B %d, %Y -- %H:%M:%S', time.localtime(date_modified))

            section = new_post_section(title, msg, 'html/' + html_filename, img, date)
            sections[section] = time.localtime(date_modified)

# sort the sections based on the file creation/modification time
sections_html = ''.join(sorted(sections, key=sections.__getitem__, reverse=True))

# write the index file
with open('index.html', 'w') as fh:
    fh.write(get_head_and_body() +
             post_section_start +
             sections_html +
             post_section_end +
             body_end
             )
