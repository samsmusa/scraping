import scrapy
from tqdm import tqdm

class freelancer_job(scrapy.Spider):
    name = 'jobs'
    start_urls = ['https://www.freelancer.com.bd/jobs/']

    def parse(self, response):
        for job in response.xpath('//*[@id="project-list"]/div'):
            yield {
                'title':job.css('a.JobSearchCard-primary-heading-link::text').get().strip(),
                'description':job.css('p.JobSearchCard-primary-description::text').get().strip(),
                'days left':job.css('span.JobSearchCard-primary-heading-days::text').get().strip(),
                'price':job.css('div.JobSearchCard-primary-price::text').get().strip(),
                'tags':job.css('a.JobSearchCard-primary-tagsLink::text').extract()
            }

        for i in range(2,200):
            next_page = f'https://www.freelancer.com.bd/jobs/{i}/'
            yield scrapy.Request(next_page, callback=self.parse)