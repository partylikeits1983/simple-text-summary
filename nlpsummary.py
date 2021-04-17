from transformers import pipeline

# using pipeline API for summarization task
summarization = pipeline("summarization")


original_text = """
Retail Sales, Manufacturing Slip Ahead of Expected Spring Rebound - WSJ

U.S. ECONOMY

Retail Sales, Manufacturing Slip Ahead of Expected
Spring Rebound
U.S. shoppers pulled back and factories produced less in February due to winter weather and supplychain disruptions

U.S. retailers and manufacturers slumped in February due to winter storms and supplychain disruptions, but a broader economic rebound appears poised to accelerate this
spring because of the easing pandemic and another round of government stimulus.
Retail sales—a measure of purchases at stores, at restaurants and online—fell by 3% in
February compared with the prior month, the Commerce Department said Tuesday. The
decline followed robust January sales that were propelled by stimulus payments to
households from the December pandemic-relief package. January sales advanced a
revised 7.6%, up from the earlier estimate of a 5.3% increase.

Severe winter weather wreaked havoc across a large swath of the U.S., aﬀecting retail
shopping and manufacturing output last month. The Federal Reserve separately said
industrial production fell a seasonally adjusted 2.2% in February compared with January.
Manufacturing, the largest component in the industrial-production index, drove the
decline because of the weather disruptions and supply shortages in semiconductors for
autos, the Fed said.

Consumers meanwhile spent less on autos, furniture, electronics, home improvement,
healthcare and clothing. Sales at food and beverage stores were unchanged, while sales at
gas stations were up strongly, by 3.6%, as gas prices have accelerated this year.
Despite the February decline, retail sales were up 6% over the last three months compared
with the same period a year earlier, according to the Commerce Department.
February is typically a quiet month for retail sales, as stores gear up for the spring selling
season, including Easter. Economists expect spending to accelerate in the coming months
as additional government stimulus is distributed and Covid-19 vaccinations lead to a
corresponding decline in cases and pickup in employment levels as businesses open up
more fully.

The upwardly revised January sales ﬁgures “took the sting out of the negative surprise”
in the February data, Aneta Markowska and Thomas Simons, economists at Jeﬀeries LLC,said in a research note.

Federal stimulus checks, which many households will receive as part of the $1.9 trillion
coronavirus aid plan signed into law last week, create “a massive tailwind for consumer
demand this spring,” the economists said.

“The checks will coincide with broadening vaccine distribution and warmer weather,
which will accelerate the return of high-contact activity, providing more avenues for
consumers to spend their stimulus payments,” they added.
JPMorgan Chase & Co.’s tracker of credit- and debit-card transactions showed consumer
spending on a seasonally adjusted basis climbed in early March after dropping oﬀ in
February.

Other signals of a pickup in the economic recovery have emerged. After cutting workers at
the end of 2020, U.S. employers added 379,000 jobs in February, and the unemployment
rate ticked down to 6.2%. The U.S. manufacturing industry has shown steady signs of
expansion.

Richard Woolley, owner at Weathered Vineyards in New Tripoli, Pa., said he was
optimistic about the outlook for business as warmer months approach and federal
stimulus eﬀorts permeate the economy.

“You can’t pump trillions of dollars into the U.S. economy and not have some of it land
here,” he said. “People will spend it. We’ll see some feedback from that at some point and
that will probably lead to an OK 2021.”
He said February was a slow month for sales, with revenue at the winery during
Valentine’s Day weekend down 50% compared with last year. Mr. Woolley said the
business is currently relying on curbside pickups and outdoor service, because of state
coronavirus mandates that restrict its ability to hold wine tastings indoors. Cold weather
last month damped the number of customers willing to sit outside, he added.

"""

summary_text = summarization(original_text)[0]['summary_text']
print("Summary:", summary_text)
