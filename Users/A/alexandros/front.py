import scraperwiki
import urlparse

scraperwiki.sqlite.attach('ln') 
data =  scraperwiki.sqlite.select('* from `ln`.swdata')

print """<html>
    <head>
        <title>LumpNet</title>
        <style>
            /**
             * HTML5 ✰ Boilerplate
             *
             * style.css contains a reset, font normalization and some base styles.
             *
             * Credit is left where credit is due.
             * Much inspiration was taken from these projects:
             * - yui.yahooapis.com/2.8.1/build/base/base.css
             * - camendesign.com/design/
             * - praegnanz.de/weblog/htmlcssjs-kickstart
             */
            
            
            /**
             * html5doctor.com Reset Stylesheet (Eric Meyer's Reset Reloaded + HTML5 baseline)
             * v1.6.1 2010-09-17 | Authors: Eric Meyer & Richard Clark
             * html5doctor.com/html-5-reset-stylesheet/
             */
            
            html, body, div, span, object, iframe,
            h1, h2, h3, h4, h5, h6, p, blockquote, pre,
            abbr, address, cite, code, del, dfn, em, img, ins, kbd, q, samp,
            small, strong, sub, sup, var, b, i, dl, dt, dd, ol, ul, li,
            fieldset, form, label, legend,
            table, caption, tbody, tfoot, thead, tr, th, td,
            article, aside, canvas, details, figcaption, figure,
            footer, header, hgroup, menu, nav, section, summary,
            time, mark, audio, video {
              margin: 0;
              padding: 0;
              border: 0;
              font-size: 100%;
              font: inherit;
              vertical-align: baseline;
            }
            
            article, aside, details, figcaption, figure,
            footer, header, hgroup, menu, nav, section {
              display: block;
            }
            
            blockquote, q { quotes: none; }
            
            blockquote:before, blockquote:after,
            q:before, q:after { content: ""; content: none; }
            
            ins { background-color: #ff9; color: #000; text-decoration: none; }
            
            mark { background-color: #ff9; color: #000; font-style: italic; font-weight: bold; }
            
            del { text-decoration: line-through; }
            
            abbr[title], dfn[title] { border-bottom: 1px dotted; cursor: help; }
            
            table { border-collapse: collapse; border-spacing: 0; }
            
            hr { display: block; height: 1px; border: 0; border-top: 1px solid #ccc; margin: 1em 0; padding: 0; }
            
            input, select { vertical-align: middle; }
            
            
            /**
             * Font normalization inspired by YUI Library's fonts.css: developer.yahoo.com/yui/
             */
            
            body { font:17px/1.231 sans-serif; *font-size:small; } /* Hack retained to preserve specificity */
            select, input, textarea, button { font:99% sans-serif; }
            
            /* Normalize monospace sizing:
               en.wikipedia.org/wiki/MediaWiki_talk:Common.css/Archive_11#Teletype_style_fix_for_Chrome */
            pre, code, kbd, samp { font-family: monospace, sans-serif; }
            
            
            /**
             * Minimal base styles.
             */
            
            /* Always force a scrollbar in non-IE */
            html { overflow-y: scroll; }
            
            /* Accessible focus treatment: people.opera.com/patrickl/experiments/keyboard/test */
            a:hover, a:active { outline: none; }
            
            ul, ol { margin-left: 2em; }
            ol { list-style-type: decimal; }
            
            /* Remove margins for navigation lists */
            nav ul, nav li { margin: 0; list-style:none; list-style-image: none; }
            
            small { font-size: 85%; }
            strong, th { font-weight: bold; }
            
            td { vertical-align: top; }
            
            /* Set sub, sup without affecting line-height: gist.github.com/413930 */
            sub, sup { font-size: 75%; line-height: 0; position: relative; }
            sup { top: -0.5em; }
            sub { bottom: -0.25em; }
            
            pre {
              /* www.pathf.com/blogs/2008/05/formatting-quoted-code-in-blog-posts-css21-white-space-pre-wrap/ */
              white-space: pre; white-space: pre-wrap; word-wrap: break-word;
              padding: 15px;
            }
            
            textarea { overflow: auto; } /* www.sitepoint.com/blogs/2010/08/20/ie-remove-textarea-scrollbars/ */
            
            .ie6 legend, .ie7 legend { margin-left: -7px; } 
            
            /* Align checkboxes, radios, text inputs with their label by: Thierry Koblentz tjkdesign.com/ez-css/css/base.css  */
            input[type="radio"] { vertical-align: text-bottom; }
            input[type="checkbox"] { vertical-align: bottom; }
            .ie7 input[type="checkbox"] { vertical-align: baseline; }
            .ie6 input { vertical-align: text-bottom; }
            
            /* Hand cursor on clickable input elements */
            label, input[type="button"], input[type="submit"], input[type="image"], button { cursor: pointer; }
            
            /* Webkit browsers add a 2px margin outside the chrome of form elements */
            button, input, select, textarea { margin: 0; }
            
            /* Colors for form validity */
            input:valid, textarea:valid   {  }
            input:invalid, textarea:invalid {
               border-radius: 1px; -moz-box-shadow: 0px 0px 5px red; -webkit-box-shadow: 0px 0px 5px red; box-shadow: 0px 0px 5px red;
            }
            .no-boxshadow input:invalid, .no-boxshadow textarea:invalid { background-color: #f0dddd; }
            
            
            /* These selection declarations have to be separate
               No text-shadow: twitter.com/miketaylr/status/12228805301 */
            ::-moz-selection{ background: #00AC00; color:#fff; text-shadow: none; }
            ::selection { background:#00AC00; color:#fff; text-shadow: none; }
            
            /* j.mp/webkit-tap-highlight-color */
            a:link { -webkit-tap-highlight-color: #FF5E99; }
            
            /* Make buttons play nice in IE:
               www.viget.com/inspire/styling-the-button-element-in-internet-explorer/ */
            button {  width: auto; overflow: visible; }
            
            /* Bicubic resizing for non-native sized IMG:
               code.flickr.com/blog/2008/11/12/on-ui-quality-the-little-things-client-side-image-resizing/ */
            .ie7 img { -ms-interpolation-mode: bicubic; }
            
            /**
             * You might tweak these..
             */
            
            body, select, input, textarea {
              /* #444 looks better than black: twitter.com/H_FJ/statuses/11800719859 */
              color: #444;
              /* Set your base font here, to apply evenly */
              /* font-family: Georgia, serif;  */
            }
            
            /* Headers (h1, h2, etc) have no default font-size or margin; define those yourself */
            h1, h2, h3, h4, h5, h6 { font-weight: bold; }
            
            a, a:active { color: #000000 }
            a:visited { color: #999999; }
            a:hover { color: #AAAAAA; }
            
            /**
             * Primary styles
             *
             * Author: 
             */
            
            table.top{
                margin-left: auto; 
                margin-right: auto; 
                width: 780px; 
            }
            
            .top tr.underl{
                border-bottom: solid 1px;
                border-color: #00AC00;
            }
            
            .top td{
                padding:5px 0px
            }
            
            table.main{
                margin-left: auto; 
                margin-right: auto; 
                width: 780px; 
            }
            
            table.main td{
                padding-bottom: 25px;
            }
            
            td.lrg{
                width: 80px;
            }
            
            div.lrg{
                font-size: 130%;
                text-align: center;
                border-collapse:separate;
                border-radius: 15px 0px 15px 0px;
                -moz-border-radius: 15px 0px 15px 0px;
                -webkit-border-radius: 15px 0px 15px 0px;
                color: #777777;
                height: 45px;
                border: solid 1px;
                border-color: #00AC00;
                /*background-color:#DDEEDD;*/
            }
            
            .mid{
                padding: 0px 10px;
            }
            
            .sml{
                font-size: 70%;
            }
            
            .arrow-up {
                width: 0;
                height: 0;
                border-left: 6px solid transparent;
                border-right: 6px solid transparent;
                border-bottom: 12px solid #77AC77
            }
            
            .arrow-down {
                width: 0;
                height: 0;
                border-left: 6px solid transparent;
                border-right: 6px solid transparent;
                border-top: 12px solid #77AC77;
            }
            
            .circle {
                width: 12px;
                height: 12px;
                background: #77AC77;
                border-radius: 6px;
                -moz-border-radius: 6px;
                -webkit-border-radius: 6px;
            }
            
            .shapebox{
                padding:2px;
            }
            
            /**
             * Non-semantic helper classes: please define your styles before this section.
             */
            
            /* For image replacement */
            .ir { display: block; text-indent: -999em; overflow: hidden; background-repeat: no-repeat; text-align: left; direction: ltr; }
            
            /* Hide for both screenreaders and browsers:
               css-discuss.incutio.com/wiki/Screenreader_Visibility */
            .hidden { display: none; visibility: hidden; }
            
            /* Hide only visually, but have it available for screenreaders: by Jon Neal.
              www.webaim.org/techniques/css/invisiblecontent/  &  j.mp/visuallyhidden */
            .visuallyhidden { border: 0; clip: rect(0 0 0 0); height: 1px; margin: -1px; overflow: hidden; padding: 0; position: absolute; width: 1px; }
            /* Extends the .visuallyhidden class to allow the element to be focusable when navigated to via the keyboard: drupal.org/node/897638 */
            .visuallyhidden.focusable:active,
            .visuallyhidden.focusable:focus { clip: auto; height: auto; margin: 0; overflow: visible; position: static; width: auto; }
            
            /* Hide visually and from screenreaders, but maintain layout */
            .invisible { visibility: hidden; }
            
            /* The Magnificent Clearfix: Updated to prevent margin-collapsing on child elements.
               j.mp/bestclearfix */
            .clearfix:before, .clearfix:after { content: "\0020"; display: block; height: 0; overflow: hidden; }
            .clearfix:after { clear: both; }
            /* Fix clearfix: blueprintcss.lighthouseapp.com/projects/15318/tickets/5-extra-margin-padding-bottom-of-page */
            .clearfix { zoom: 1; }
            
            
            
            /**
             * Media queries for responsive design.
             *
             * These follow after primary styles so they will successfully override.
             */
            
            @media all and (orientation:portrait) {
              /* Style adjustments for portrait mode goes here */
            
            }
            
            @media all and (orientation:landscape) {
              /* Style adjustments for landscape mode goes here */
            
            }
            
            /* Grade-A Mobile Browsers (Opera Mobile, Mobile Safari, Android Chrome)
               consider this: www.cloudfour.com/css-media-query-for-mobile-is-fools-gold/ */
            @media screen and (max-device-width: 480px) {
            
            
              /* Uncomment if you don't want iOS and WinMobile to mobile-optimize the text for you: j.mp/textsizeadjust */
              /* html { -webkit-text-size-adjust:none; -ms-text-size-adjust:none; } */
            }
            
            
            /**
             * Print styles.
             *
             * Inlined to avoid required HTTP connection: www.phpied.com/delay-loading-your-print-css/
             */
            @media print {
              * { background: transparent !important; color: black !important; text-shadow: none !important; filter:none !important;
              -ms-filter: none !important; } /* Black prints faster: sanbeiji.com/archives/953 */
              a, a:visited { color: #444 !important; text-decoration: underline; }
              a[href]:after { content: " (" attr(href) ")"; }
              abbr[title]:after { content: " (" attr(title) ")"; }
              .ir a:after, a[href^="javascript:"]:after, a[href^="#"]:after { content: ""; }  /* Don't show links for images, or javascript/internal links */
              pre, blockquote { border: 1px solid #999; page-break-inside: avoid; }
              thead { display: table-header-group; } /* css-discuss.incutio.com/wiki/Printing_Tables */
              tr, img { page-break-inside: avoid; }
              @page { margin: 0.5cm; }
              p, h2, h3 { orphans: 3; widows: 3; }
              h2, h3{ page-break-after: avoid; }
            }
            
        </style>
        
    </head>
    <body>
        <table class='top'>
            <tr class='underl'>
                <td style='vertical-align:bottom'>
                    <div align='left'><strong>LumpNet</strong></div>
                </td>
                <td style='vertical-align:bottom'>
                    <div align='right'><span class='sml'>Alexandros (log out)</span></div>
                </td>
            </tr>
            <tr>
                <td colspan='2'>
                    <div align='right'><span class='sml'>submit | voted</span></div>
                </td>
            </tr>
        </table>
        <table class='main'>"""

for item in data:
    #print item
    pct = round(float(item['score'])*100, 1)
    #print item['score'],pct
    print """            <tr>
                <td>                    
                    <div class='shapebox'><div class='arrow-up'></div></div>
                    <div class='shapebox'><div class='circle'></div></div>
                    <div class='shapebox'><div class='arrow-down'></div></div>
                </td>
                <td class='lrg'>
                    <div class='lrg'><p style='line-height:2em'>%s%%</p></div>
                </td>
                <td class='mid' style='vertical-align:middle'>
                    <a href='%s'>%s</a> <span class='sml'>Source: %s<br/>
                    Submitted by: %s, Value: %s, Age: %s, Score: %s</span>
                </td>
            </tr>""" % (pct, item['uri'], item['title'], urlparse.urlparse(item['uri']).hostname, item['user'], item['value'], item['age'], item['score'])

print"""        </table>
    </body>
</html>"""