<?php
require 'scraperwiki/simple_html_dom.php';

// for ($i=1;$i<68;++$i) {
//    $html_content = scraperwiki::scrape("http://www.zodynas.lt/tarptautiniu-zodziu/?page=".$i);
//    $html = str_get_html($html_content);
//    foreach ($html->find("ul.abc_list li") as $el) {
//        $word = trim(str_replace(' ','',$el->find('a',0)->innertext),'.- \r\n\0\x0B\t');
//        $word_full = trim($el->find('a',0)->innertext,'.- \r\n\0\x0B\t');
//        $link = $el->find('a',0)->href;
//        $desc = '';
//        scraperwiki::save_sqlite(array("word"),array("word"=>$word, "link"=>$link,"description"=>$desc));
//    }
//    $html->__destruct();
//} 
//scraperwiki::sqlitecommit(); 
$count = 0;
while($db = scraperwiki::select("* from swdata where description IS NULL OR description = '' order by random() limit 1")) {
        $html_content_2 = scraperwiki::scrape("http://www.zodynas.lt".$db[0]['link']);
        $html_2 = str_get_html($html_content_2);
        $el = $html_2->find('h1',0);
        if ($el) {
            $el2 = $el->next_sibling();
            if ($el2) {
                $desc = trim($el2->plaintext);
                $desc = explode(',',$desc,2);
                $desc = array_pop($desc);
                scraperwiki::save_sqlite(array("word"),array("word"=>$db[0]['word'], "link"=>$db[0]['link'],"description"=>$desc));
                ++$count;
            }
        }
        //if ($count>10) break;
} 
        //print $word.'|'.$link.'|'.$desc.'\r';


?>
