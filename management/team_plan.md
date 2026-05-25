# Team Management Plan

## Project Title

Mapping AI Job Replacement Anxiety on Reddit: A Social Media and Network Analysis of Career Concerns, Sentiment, Topics, and Influential Discussion Communities

## Team Size

This project is completed by a team of two students. Although the assignment recommends groups of three, a two-person team is allowed. The project scope is kept realistic by focusing on one social media platform, Reddit, and by combining one main NLP pipeline with one meaningful network analysis component.

## Team Members

| Member | Student ID | Main Role |
|---|---|---|
| Member 1 | Add student ID | Data Collection and NLP Analysis |
| Member 2 | Add student ID | Network Analysis and Report/Presentation |

## Role Allocation

### Member 1: Data Collection and NLP Analysis

Responsibilities:
- Set up Reddit API/PRAW or alternative data collection process
- Collect Reddit posts and comments
- Clean and preprocess text
- Perform keyword and bigram analysis
- Apply VADER sentiment analysis
- Run LDA topic modelling
- Produce NLP figures and tables
- Write data collection, preprocessing, and NLP methodology sections

### Member 2: Network Analysis and Communication

Responsibilities:
- Build Reddit reply network
- Define nodes, edges, direction, and weight
- Calculate centrality measures
- Run Louvain community detection
- Produce network visualisations and centrality tables
- Write network methodology and analysis sections
- Prepare report formatting and presentation slides

## Shared Responsibilities

Both members will:
- Review the research questions
- Check code and results
- Contribute to the final discussion and conclusion
- Proofread the final report
- Practise and deliver the presentation
- Maintain files in the shared repository

## Weekly Project Plan

| Week | Planned Work | Responsible Member(s) | Evidence |
|---|---|---|---|
| Week 1 | Finalise topic, research questions, success criteria, and repository setup | Both | README, project plan |
| Week 2 | Collect Reddit posts and comments | Member 1 | Raw dataset, data collection script |
| Week 3 | Clean dataset and prepare text for analysis | Member 1 | Cleaned dataset, preprocessing script |
| Week 4 | Run keyword, bigram, and sentiment analysis | Member 1 | Figures, sentiment table |
| Week 5 | Run LDA topic modelling and choose final number of topics | Member 1 | Topic table, coherence results |
| Week 6 | Build Reddit reply network and calculate centrality | Member 2 | Network file, centrality table |
| Week 7 | Run community detection and create network visualisations | Member 2 | Community table, graph images |
| Week 8 | Write first full report draft | Both | Draft report |
| Week 9 | Improve discussion, limitations, references, and formatting | Both | Updated report |
| Week 10 | Prepare presentation slides and speaking script | Both | Slides, script |
| Final Week | Final proofreading, export PDF, check submission files | Both | Final submission package |

## Meeting Log

| Date | Meeting Type | Attendees | Main Decisions | Action Items |
|---|---|---|---|---|
| Add date | Online/In-person | Both | Topic selected: AI job replacement anxiety on Reddit | Create repo and project folders |
| Add date | Online/In-person | Both | Research questions and methods confirmed | Begin data collection |
| Add date | Online/In-person | Both | NLP results reviewed | Start network analysis |
| Add date | Online/In-person | Both | Network results reviewed | Start report draft |
| Add date | Online/In-person | Both | Final report and slides reviewed | Submit final files |

## Timesheet Template

| Week | Member | Task | Hours Spent | Evidence |
|---|---|---|---|---|
| Week 1 | Member 1 | Topic planning and repository setup | 2 | README |
| Week 1 | Member 2 | Topic planning and project plan | 2 | team_plan.md |
| Week 2 | Member 1 | Data collection | Add hours | Script/dataset |
| Week 2 | Member 2 | Data collection support and documentation | Add hours | Notes/report draft |
| Week 3 | Member 1 | Data cleaning | Add hours | Cleaned dataset |
| Week 3 | Member 2 | Network design planning | Add hours | Network design notes |

## Risk Management

| Risk | Impact | Mitigation |
|---|---|---|
| Reddit API access issues | Data collection may be delayed | Use smaller dataset, public Reddit exports, or manually collected sample if needed |
| Dataset too large | Code may become slow | Limit to relevant subreddits and 1,500–3,000 posts/comments |
| Dataset too small | Analysis may lack depth | Expand keywords or add another subreddit |
| Sentiment results inaccurate due to sarcasm | May affect interpretation | Mention this as a limitation and inspect sample comments manually |
| Network too sparse | Centrality/community results may be weak | Filter for posts with comment threads and enough reply interactions |
| Unequal contribution | Teamwork marks may be affected | Maintain weekly timesheets and clear evidence of work |

## Communication Plan

The team will communicate through:
- Messenger/WhatsApp for quick updates
- GitHub or shared cloud folder for files
- Weekly meeting notes for progress tracking
- VS Code/Jupyter for code development

## Repository Management

The repository will include:
- Code files
- Notebook
- Cleaned sample data
- Figures
- Report draft
- Team management files
- Presentation files

No private API keys, passwords, access tokens, or credentials will be committed to the repository.

## Individual Reflection Template

### Member 1 Reflection

My main contribution was data collection and NLP analysis. I worked on collecting Reddit posts and comments, cleaning the text, and applying keyword, bigram, sentiment, and topic modelling methods. I learned how social media text needs significant preprocessing before analysis and how topic modelling can reveal hidden themes in online discussions. One challenge was dealing with noisy Reddit text and irrelevant comments. I addressed this by applying cleaning, stopword removal, and filtering steps.

### Member 2 Reflection

My main contribution was network analysis and communication of results. I constructed the Reddit reply network, calculated centrality measures, detected communities, and helped prepare the report and presentation. I learned how user interactions can be represented as a graph and how centrality measures help identify influential or bridging users. One challenge was making the network meaningful rather than just visual. I addressed this by clearly defining nodes, edges, direction, edge weight, and relevant network measures.