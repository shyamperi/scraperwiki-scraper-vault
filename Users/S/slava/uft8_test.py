import scraperwiki

data = {'branch_name': u'\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043e\u0444\u0438\u0441 \xab\u0421\u043e\u043b\u043d\u0435\u0447\u043d\u044b\u0439\xbb \u041e\u0410\u041e \xab\u0423\u0411\u0420\u0438\u0420\xbb', 'address': u'620109, \u0421\u0432\u0435\u0440\u0434\u043b\u043e\u0432\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c, \u0433. \u0415\u043a\u0430\u0442\u0435\u0440\u0438\u043d\u0431\u0443\u0440\u0433, \u0443\u043b. \u041a\u0440\u0430\u0443\u043b\u044f, \u0434. 44'}

print data['branch_name'].encode('utf-8')
