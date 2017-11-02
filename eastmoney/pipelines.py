# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from eastmoney.moulding_board.mypipelines import GeneralMysqlPipeline


class EastmoneyPipeline(object):
    def process_item(self, item, spider):
        return item


class EastmoneyNewsPipeline(GeneralMysqlPipeline):
    def process_item(self, item, spider):
        item = dict(item)
        if item['title']:
            try:
                # 最好写一行,否则容易报错
                count = self.cs.execute(f'''insert into news_bloom(title, abstract, stocks, content, url) values("""{item['title']}""","""{item['abstract']}""","""{item['stocks']}""", """{item['content']}""", """{item['url']}""");''')
                if count:
                    self.conn.commit()
            except Exception as error:
                print('error------------------------>', error)
        return item

def main():
    item = dict()
    item['title'] = '3'
    item['abstract'] = '3'
    item['stocks'] = '3'
    print(f'''insert into news(title, abstract, stocks, content) "
    "values("{item['title']}","{item['abstract']}","{item['stocks']}","{item['content']}");''')


if __name__ == '__main__':
    main()
