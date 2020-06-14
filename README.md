# news.liverpool.ac.uk to XML/RSS aggregator
A python3 script used to scrape the news from the https://news.liverpool.ac.uk/category/press-release/ and display the data as XML/RSS compatible.

Sample of the output:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:dc="http://purl.org/dc/elements/1.1/">
    <channel>
        <title>News Liverpool RSS Feed</title>
        <link>https://news.liverpool.ac.uk/category/press-release/</link>
        <description>News Aggregated from news.liverpool.ac.uk</description>
        <language>en-US</language>
        <lastBuildDate>Sun, 14 Jun 2020 16:26:46 GMT</lastBuildDate>
        <generator>rfeed v1.1.1</generator>
        <docs>https://github.com/svpino/rfeed/blob/master/README.md</docs>
        <item>
            <title>New episode of ‘The Coping with COVID’ podcast now available</title>
            <link>https://news.liverpool.ac.uk/2020/06/12/new-episode-of-the-coping-with-covid-podcast-now-available/</link>
            <description>In the latest episode of ‘The Coping with COVID’ podcast Dr Helen West is joined by a nursing student who has been redeployed to work in the NHS as part of the UK response to COVID-19.</description>
            <pubDate>Fri, 12 Jun 2020 01:40:00 GMT</pubDate>
            <guid isPermaLink="true">https://news.liverpool.ac.uk/2020/06/12/new-episode-of-the-coping-with-covid-podcast-now-available/</guid>
        </item>
        <item>
            <title>The University of Liverpool Maths School set to open autumn 2020</title>
            <link>https://news.liverpool.ac.uk/2020/06/12/the-university-of-liverpool-maths-school-set-to-open-autumn-2020/</link>
            <description>Plans are in place to open the University of Liverpool Maths School (ULMaS) this autumn with the recruitment of teaching staff, a formal funding agreement approved and refurbishment of accommodation underway.</description>
            <pubDate>Fri, 12 Jun 2020 10:46:00 GMT</pubDate>
            <guid isPermaLink="true">https://news.liverpool.ac.uk/2020/06/12/the-university-of-liverpool-maths-school-set-to-open-autumn-2020/</guid>
        </item>
    </channel>
</rss>

```
