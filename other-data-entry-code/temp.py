from config import db,app
from models2 import Que

# The JSON data
json_data = {
"Sheet1":[
 {
  "startup_stage": "Idea",
  "que_type": "Idea",
  "que_string": "NEWS HEADLINE: In one sentence, what is the big idea. (Hint: think newspaper headline)"
 },
 {
  "startup_stage": "Idea",
  "que_type": "Idea",
  "que_string": "What inspired you to pursue this idea, and what motivates you to see it through?"
 },
 {
  "startup_stage": "Idea",
  "que_type": "Idea",
  "que_string": "How committed are you to turning this idea into a reality, despite potential challenges?"
 },
 {
  "startup_stage": "Idea",
  "que_type": "Idea",
  "que_string": "PROBLEM: WHAT problem, specifically, does this idea address?"
 },
 {
  "startup_stage": "Idea",
  "que_type": "Idea",
  "que_string": "Solution: What is the solution to the problem?"
 },
 {
  "startup_stage": "Idea",
  "que_type": "Idea",
  "que_string": "What you dont want your idea to become? "
 },
 {
  "startup_stage": "Idea",
  "que_type": "Idea",
  "que_string": "If you had to start and launch today, what would be the first thing you would do? "
 },
 {
  "startup_stage": "Idea",
  "que_type": "Customer",
  "que_string": "Who is your target market?"
 },
 {
  "startup_stage": "Idea",
  "que_type": "Customer",
  "que_string": "How do you envision reaching and engaging with your target audience?"
 },
 {
  "startup_stage": "Idea",
  "que_type": "Customer",
  "que_string": "Promise: what’s in it for the customer? What good thing – benefit – do they get from your product? "
 },
 {
  "startup_stage": "Idea",
  "que_type": "Customer",
  "que_string": "Proof: Why would the customer believe you can deliver this promise"
 },
 {
  "startup_stage": "Idea",
  "que_type": "Customer",
  "que_string": "Payoff (dramatic difference): How will the customer's life\/ be different because of this"
 },
 {
  "startup_stage": "Idea",
  "que_type": "Competition ",
  "que_string": "Who are your main competitors, and what sets you apart from them?"
 },
 {
  "startup_stage": "Idea",
  "que_type": "Competition ",
  "que_string": "How do you plan to differentiate your offering in the market?"
 },
 {
  "startup_stage": "Idea",
  "que_type": "Risk Assessment",
  "que_string": "What are the main risks and challenges you foresee in turning your idea into a successful venture?"
 },
 {
  "startup_stage": "Idea",
  "que_type": "Risk Assessment",
  "que_string": "How do you plan to mitigate these risks?"
 },
 {
  "startup_stage": "Validation ",
  "que_type": "User Feedback",
  "que_string": "How have potential users or customers responded to your product or solution during your interactions with them?"
 },
 {
  "startup_stage": "Validation ",
  "que_type": "User Feedback",
  "que_string": "Can you share any insights or anecdotes from these conversations that have influenced your product development?"
 },
 {
  "startup_stage": "Validation ",
  "que_type": "Prototype Testing",
  "que_string": "What discoveries have you made while testing your prototype or MVP with users?"
 },
 {
  "startup_stage": "Validation ",
  "que_type": "Prototype Testing",
  "que_string": "How has user feedback influenced the evolution of your product design?"
 },
 {
  "startup_stage": "Validation ",
  "que_type": "Market Validation",
  "que_string": "What observations or patterns have emerged from your market tests or pilot programs?"
 },
 {
  "startup_stage": "Validation ",
  "que_type": "Market Validation",
  "que_string": "How do these findings inform your understanding of market demand and your product's fit within it?"
 },
 {
  "startup_stage": "Validation ",
  "que_type": "Pricing Strategy",
  "que_string": "How have discussions with potential customers informed your approach to pricing?"
 },
 {
  "startup_stage": "Validation ",
  "que_type": "Pricing Strategy",
  "que_string": "What considerations are guiding your decisions around setting the price for your product or service?"
 },
 {
  "startup_stage": "Validation ",
  "que_type": "Competitive Analysis",
  "que_string": "What insights have you gleaned from studying the competitive landscape?"
 },
 {
  "startup_stage": "Validation ",
  "que_type": "Competitive Analysis",
  "que_string": "How do you perceive your positioning relative to competitors, and what opportunities do you see for differentiation?"
 },
 {
  "startup_stage": "Validation ",
  "que_type": "Customer Acquisition Strategy",
  "que_string": "How are you thinking about attracting your first customers to your product or service?"
 },
 {
  "startup_stage": "Validation ",
  "que_type": "Customer Acquisition Strategy",
  "que_string": "Can you discuss any emerging hypotheses or strategies you're exploring to acquire and retain customers?"
 },
 {
  "startup_stage": "Validation ",
  "que_type": "Validation Metrics",
  "que_string": "What key indicators are you tracking to gauge the success of your validation efforts?"
 },
 {
  "startup_stage": "Validation ",
  "que_type": "Validation Metrics",
  "que_string": "How do you interpret fluctuations or trends in these metrics, and what actions do they prompt?"
 },
 {
  "startup_stage": "Validation ",
  "que_type": "Partnerships and Collaborations",
  "que_string": "In what ways do you envision partnerships contributing to your validation journey?"
 },
 {
  "startup_stage": "Validation ",
  "que_type": "Partnerships and Collaborations",
  "que_string": " Can you discuss any potential synergies or shared goals that might drive collaboration opportunities? "
 },
 {
  "startup_stage": "Validation ",
  "que_type": "Regulatory and Legal Considerations",
  "que_string": "How do regulatory and legal factors factor into your validation process?"
 },
 {
  "startup_stage": "Validation ",
  "que_type": "Regulatory and Legal Considerations",
  "que_string": " What strategies are you considering to navigate potential regulatory challenges or requirements? "
 },
 {
  "startup_stage": "Validation ",
  "que_type": "Iterative Approach",
  "que_string": "How are you incorporating feedback and learnings into the ongoing development of your product or business model? "
 },
 {
  "startup_stage": "Validation ",
  "que_type": "Iterative Approach",
  "que_string": "Can you describe how the iterative nature of your validation process is shaping your path forward? "
 },
 {
  "startup_stage": "Growth ",
  "que_type": "Scaling Operations",
  "que_string": "How have you scaled your operations to accommodate the growing demand for your product or service? "
 },
 {
  "startup_stage": "Growth ",
  "que_type": "Scaling Operations",
  "que_string": "Can you discuss any challenges or opportunities you've encountered while scaling, and how you've addressed them? "
 },
 {
  "startup_stage": "Growth ",
  "que_type": "Customer Acquisition and Retention",
  "que_string": "What strategies have you implemented to acquire new customers at scale? "
 },
 {
  "startup_stage": "Growth ",
  "que_type": "Customer Acquisition and Retention",
  "que_string": "How do you approach customer retention and fostering loyalty as your customer base expands? "
 },
 {
  "startup_stage": "Growth ",
  "que_type": "Market Penetration",
  "que_string": "How are you penetrating new markets or segments to drive growth? "
 },
 {
  "startup_stage": "Growth ",
  "que_type": "Market Penetration",
  "que_string": "Can you share any insights or successes from your efforts to expand your market reach? "
 },
 {
  "startup_stage": "Growth ",
  "que_type": "Product Development Roadmap",
  "que_string": "How does your product development roadmap align with your growth objectives? "
 },
 {
  "startup_stage": "Growth ",
  "que_type": "Product Development Roadmap",
  "que_string": "What new features or enhancements are you prioritizing to meet the evolving needs of your expanding customer base? "
 },
 {
  "startup_stage": "Growth ",
  "que_type": "Team Expansion and Development",
  "que_string": "How has your team evolved to support the company's growth trajectory? "
 },
 {
  "startup_stage": "Growth ",
  "que_type": "Team Expansion and Development",
  "que_string": "What initiatives or investments have you made in talent acquisition, training, and development? "
 },
 {
  "startup_stage": "Growth ",
  "que_type": "Partnership and Collaboration Opportunities",
  "que_string": "How do you leverage partnerships and collaborations to fuel growth? "
 },
 {
  "startup_stage": "Growth ",
  "que_type": "Partnership and Collaboration Opportunities",
  "que_string": "Can you discuss any recent or upcoming partnerships that are strategic to your growth strategy? "
 },
 {
  "startup_stage": "Growth ",
  "que_type": "Revenue Growth and Monetization Strategies",
  "que_string": "How has your revenue grown since the launch phase, and what factors have contributed to this growth? "
 },
 {
  "startup_stage": "Growth ",
  "que_type": "Revenue Growth and Monetization Strategies",
  "que_string": "What monetization strategies are you employing to capture value from your expanding customer base? "
 },
 {
  "startup_stage": "Growth ",
  "que_type": "Customer Feedback Integration",
  "que_string": "How do you continue to incorporate customer feedback into your growth strategy? "
 },
 {
  "startup_stage": "Growth ",
  "que_type": "Customer Feedback Integration",
  "que_string": "Can you share any examples of how customer insights have influenced strategic decisions or product enhancements? "
 },
 {
  "startup_stage": "Growth ",
  "que_type": "Scalability Challenges",
  "que_string": "What scalability challenges have emerged as you've experienced rapid growth, and how are you addressing them? "
 },
 {
  "startup_stage": "Growth ",
  "que_type": "Scalability Challenges",
  "que_string": "Are there any areas of your business or operations that require particular attention to ensure continued scalability? "
 },
 {
  "startup_stage": "Growth ",
  "que_type": "Competitive Landscape Dynamics",
  "que_string": "How has the competitive landscape evolved as you've grown, and how do you maintain a competitive edge? "
 },
 {
  "startup_stage": "Growth ",
  "que_type": "Competitive Landscape Dynamics",
  "que_string": "Can you discuss any competitive strategies or responses to market shifts that have been instrumental in sustaining growth?"
 },
 {
  "startup_stage": "Expansion ",
  "que_type": "Market Expansion Strategy",
  "que_string": "How are you planning to expand into new markets or geographic regions? "
 },
 {
  "startup_stage": "Expansion ",
  "que_type": "Market Expansion Strategy",
  "que_string": "Can you discuss the rationale behind your expansion strategy and the opportunities you see in these new markets? "
 },
 {
  "startup_stage": "Expansion ",
  "que_type": "Product or Service Diversification",
  "que_string": "Are you considering diversifying your product or service offerings to capture additional market segments or address new customer needs?"
 },
 {
  "startup_stage": "Expansion ",
  "que_type": "Product or Service Diversification",
  "que_string": "How do you prioritize and evaluate opportunities for product diversification?"
 },
 {
  "startup_stage": "Expansion ",
  "que_type": "International Growth Considerations",
  "que_string": "If applicable, how are you approaching international expansion?"
 },
 {
  "startup_stage": "Expansion ",
  "que_type": "International Growth Considerations",
  "que_string": "What challenges or opportunities do you anticipate in entering new international markets?"
 },
 {
  "startup_stage": "Expansion ",
  "que_type": "Partnership and Distribution Channels",
  "que_string": "How do you leverage partnerships and alternative distribution channels to facilitate expansion?"
 },
 {
  "startup_stage": "Expansion ",
  "que_type": "Partnership and Distribution Channels",
  "que_string": "Can you discuss any recent or planned partnerships that support your expansion efforts?"
 },
 {
  "startup_stage": "Expansion ",
  "que_type": "Operational Scalability",
  "que_string": "How have you ensured that your operations can scale effectively to support the increased demands of expansion?"
 },
 {
  "startup_stage": "Expansion ",
  "que_type": "Operational Scalability",
  "que_string": "What measures have you taken to optimize efficiency and manage costs as you grow?"
 },
 {
  "startup_stage": "Expansion ",
  "que_type": "Customer Acquisition Strategies in New Markets",
  "que_string": "How do your customer acquisition strategies differ in new markets compared to your existing ones?"
 },
 {
  "startup_stage": "Expansion ",
  "que_type": "Customer Acquisition Strategies in New Markets",
  "que_string": "Can you share any insights or successes from your efforts to establish a presence in new markets?"
 },
 {
  "startup_stage": "Expansion ",
  "que_type": "Cultural Adaptation and Localization",
  "que_string": "How do you approach adapting your product or service to suit the cultural nuances of new markets?"
 },
 {
  "startup_stage": "Expansion ",
  "que_type": "Cultural Adaptation and Localization",
  "que_string": "What strategies do you employ to ensure your brand resonates with diverse audiences?"
 },
 {
  "startup_stage": "Expansion ",
  "que_type": "Regulatory and Compliance Considerations",
  "que_string": "How do you navigate regulatory and compliance requirements when expanding into new markets?"
 },
 {
  "startup_stage": "Expansion ",
  "que_type": "Regulatory and Compliance Considerations",
  "que_string": "Can you discuss any specific challenges or approaches to regulatory compliance in different regions?"
 },
 {
  "startup_stage": "Expansion ",
  "que_type": "Competitive Landscape Analysis",
  "que_string": "How does the competitive landscape differ in the markets you're expanding into compared to your existing markets?"
 },
 {
  "startup_stage": "Expansion ",
  "que_type": "Competitive Landscape Analysis",
  "que_string": "How do you maintain a competitive advantage as you enter new territories or sectors?"
 },
 {
  "startup_stage": "Expansion ",
  "que_type": "Success Metrics for Expansion",
  "que_string": "What key performance indicators (KPIs) are you tracking to measure the success of your expansion efforts?"
 },
 {
  "startup_stage": "Expansion ",
  "que_type": "Success Metrics for Expansion",
  "que_string": "How do you evaluate the ROI of expansion initiatives and adjust strategies accordingly?"
 },
 {
  "startup_stage": "Maturity ",
  "que_type": "Market Position and Competitive Advantage",
  "que_string": "How do you perceive your current position within the market, and what sets you apart from competitors?"
 },
 {
  "startup_stage": "Maturity ",
  "que_type": "Market Position and Competitive Advantage",
  "que_string": "Can you discuss the strengths and advantages that have contributed to your success in reaching the maturity stage?"
 },
 {
  "startup_stage": "Maturity ",
  "que_type": "Customer Loyalty and Satisfaction",
  "que_string": "How do you foster customer loyalty and maintain high levels of customer satisfaction at this stage?"
 },
 {
  "startup_stage": "Maturity ",
  "que_type": "Customer Loyalty and Satisfaction",
  "que_string": "Can you share insights into the factors that contribute to customer retention and loyalty over time?"
 },
 {
  "startup_stage": "Maturity ",
  "que_type": "Revenue and Profitability Growth",
  "que_string": "How has your revenue and profitability evolved since the earlier stages of the startup?"
 },
 {
  "startup_stage": "Maturity ",
  "que_type": "Revenue and Profitability Growth",
  "que_string": "What strategies have you implemented to sustain revenue growth and ensure profitability in the maturity stage?"
 },
 {
  "startup_stage": "Maturity ",
  "que_type": "Innovation and Product Development",
  "que_string": "How do you continue to innovate and evolve your product or service offerings in the maturity stage?"
 },
 {
  "startup_stage": "Maturity ",
  "que_type": "Innovation and Product Development",
  "que_string": "Can you discuss any recent product developments or enhancements that have been instrumental in maintaining competitiveness?"
 },
 {
  "startup_stage": "Maturity ",
  "que_type": "Market Share and Expansion Opportunities",
  "que_string": "What is your current market share, and how do you plan to sustain or expand it in the mature market?"
 },
 {
  "startup_stage": "Maturity ",
  "que_type": "Market Share and Expansion Opportunities",
  "que_string": "Are there any untapped market segments or opportunities for further expansion?"
 },
 {
  "startup_stage": "Maturity ",
  "que_type": "Operational Efficiency and Optimization",
  "que_string": "How do you optimize your operations to maintain efficiency and manage costs effectively?"
 },
 {
  "startup_stage": "Maturity ",
  "que_type": "Operational Efficiency and Optimization",
  "que_string": "Can you share any initiatives or strategies aimed at streamlining processes and improving productivity?"
 },
 {
  "startup_stage": "Maturity ",
  "que_type": "Brand Reputation and Trust",
  "que_string": "How have you cultivated and protected your brand reputation over time?"
 },
 {
  "startup_stage": "Maturity ",
  "que_type": "Brand Reputation and Trust",
  "que_string": "What measures do you take to ensure trust and credibility among customers, partners, and stakeholders?"
 },
 {
  "startup_stage": "Maturity ",
  "que_type": "Talent Management and Organizational Culture",
  "que_string": "How do you attract and retain top talent in the maturity stage?"
 },
 {
  "startup_stage": "Maturity ",
  "que_type": "Talent Management and Organizational Culture",
  "que_string": "Can you discuss the role of organizational culture in sustaining success and fostering innovation?"
 },
 {
  "startup_stage": "Maturity ",
  "que_type": "Risk Management and Resilience",
  "que_string": "How do you identify and mitigate risks to ensure long-term sustainability?"
 },
 {
  "startup_stage": "Maturity ",
  "que_type": "Risk Management and Resilience",
  "que_string": "Can you share examples of how you've navigated challenges or disruptions in the mature market?"
 },
 {
  "startup_stage": "Maturity ",
  "que_type": "Future Growth Strategies and Evolution",
  "que_string": "What is your vision for the future growth and evolution of the company beyond the maturity stage?"
 },
 {
  "startup_stage": "Maturity ",
  "que_type": "Future Growth Strategies and Evolution",
  "que_string": "How do you adapt your strategies to stay relevant and seize new opportunities in a changing market landscape?"
 },
 {
  "startup_stage": "Exit ",
  "que_type": "Exit Strategy and Objectives",
  "que_string": "What is your primary objective for pursuing an exit at this stage?"
 },
 {
  "startup_stage": "Exit ",
  "que_type": "Exit Strategy and Objectives",
  "que_string": "Can you discuss the rationale behind your chosen exit strategy (e.g., acquisition, merger, IPO)?"
 },
 {
  "startup_stage": "Exit ",
  "que_type": "Company Valuation and Value Proposition",
  "que_string": "How do you assess the current valuation of the company, and what factors contribute to its value proposition?"
 },
 {
  "startup_stage": "Exit ",
  "que_type": "Company Valuation and Value Proposition",
  "que_string": "Can you highlight any unique strengths or assets that make the company attractive to potential buyers or investors?"
 },
 {
  "startup_stage": "Exit ",
  "que_type": "Market and Industry Dynamics",
  "que_string": "How do market trends and industry dynamics influence your decision to pursue an exit at this time?"
 },
 {
  "startup_stage": "Exit ",
  "que_type": "Market and Industry Dynamics",
  "que_string": "Can you discuss any external factors or market conditions that impact the timing and feasibility of the exit?"
 },
 {
  "startup_stage": "Exit ",
  "que_type": "Stakeholder Alignment and Communication",
  "que_string": "How do you ensure alignment among stakeholders regarding the exit process and expectations?"
 },
 {
  "startup_stage": "Exit ",
  "que_type": "Stakeholder Alignment and Communication",
  "que_string": "What communication strategies do you employ to keep stakeholders informed and engaged throughout the exit journey?"
 },
 {
  "startup_stage": "Exit ",
  "que_type": "Due Diligence Preparation",
  "que_string": "How have you prepared for the due diligence process to facilitate a smooth and efficient exit?"
 },
 {
  "startup_stage": "Exit ",
  "que_type": "Due Diligence Preparation",
  "que_string": "Can you discuss the key areas of focus and documentation required for due diligence?"
 },
 {
  "startup_stage": "Exit ",
  "que_type": "Legal and Regulatory Compliance",
  "que_string": "How do you navigate legal and regulatory considerations associated with the exit process?"
 },
 {
  "startup_stage": "Exit ",
  "que_type": "Legal and Regulatory Compliance",
  "que_string": "Can you discuss any compliance issues or regulatory hurdles that need to be addressed before completing the exit?"
 },
 {
  "startup_stage": "Exit ",
  "que_type": "Negotiation and Deal Structuring",
  "que_string": "How do you approach negotiation and deal structuring to optimize value and mitigate risks?"
 },
 {
  "startup_stage": "Exit ",
  "que_type": "Negotiation and Deal Structuring",
  "que_string": "Can you share any strategies or tactics you employ to negotiate favorable terms for the exit transaction?"
 },
 {
  "startup_stage": "Exit ",
  "que_type": "Post-Exit Transition Planning",
  "que_string": "What plans do you have in place for the transition period following the exit?"
 },
 {
  "startup_stage": "Exit ",
  "que_type": "Post-Exit Transition Planning",
  "que_string": "How do you ensure continuity and smooth integration for employees, customers, and other stakeholders post-exit?"
 },
 {
  "startup_stage": "Exit ",
  "que_type": "Financial and Tax Considerations",
  "que_string": "How do you manage financial and tax implications associated with the exit event?"
 },
 {
  "startup_stage": "Exit ",
  "que_type": "Financial and Tax Considerations",
  "que_string": "Can you discuss any strategies or advisors you engage to optimize financial outcomes and minimize tax liabilities?"
 },
 {
  "startup_stage": "Exit ",
  "que_type": "Legacy and Impact",
  "que_string": "How do you envision the legacy of the company and its impact on the industry or community post-exit?"
 },
 {
  "startup_stage": "Exit ",
  "que_type": "Legacy and Impact",
  "que_string": "Can you share any aspirations or commitments to leave a positive legacy beyond the exit transaction?"
 }
]
}

def populate_database():
    for entry in json_data["Sheet1"]:
        que_string = entry["que_string"]
        que_type = entry["que_type"]
        startup_stage = entry["startup_stage"]
        
        existing_record = Que.query.filter_by(que_string=que_string).first()
        
        if existing_record is None:
            new_que = Que(startup_stage=startup_stage, que_type=que_type, que_string=que_string)
            db.session.add(new_que)
        else:
            print(f"Duplicate entry found for que_string: {que_string}")

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        populate_database()
        print("Database populated successfully!")
