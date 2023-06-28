# Document Input→ GPT Automation

### Overview

*ChatGPT has strong query/ LLM capabilities but can not handle large documents, multiple documents, PDFs, URLs well.*  

*I want to an app to run ChatGPT across large files and multiple files.  Ideally, that doesn't require a bunch of cut and paste/ manual steps*

*Spend a week and come up with a prototype*

- Administration
    - Have a username and password
        - ability to save Open AI key
        - ability to save prompts
            - at the individual level
            - perhaps at the team level (maybe we use google docs as a hack)
        - admin super role
    - Initially local download
        - ideally able to access google drive (but there are likely permission issues)
- Level 1: Get larger files into a workable ChatGPT interface
    
    [example document](https://app.tegus.co/guest/view/tuM7wYVtj1ykx8WEGquBF8UwDS7gVKDXQpuydKV8H75Z6onX5Yn9tWhtiPz8) 
    
- Level 2: Get different types of files into a workable ChatGPT interface
    - URLs
    - PDFs
    - Google docs
    - Google slides
    - email input
        - newsletters
        - tegus call email
    - structured warehouse data inputs
    - financial research models
    - One off integrations
        - ticker→ earnings filings
        - G2
- Level 3: Access multiple files
    - run ChatGPT across 20 different documents
- Level 4: Functionality
    - memory
    - chainability
        - slack
        - email
- Level 5: organize outputs by companies- tie to a company or tie to multiple companies
- UI
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4d643d31-cb35-4a4c-845f-d1cf025c40f1/Untitled.png)
    
- Tooling/ capabilities
    - a big fan of Streamlit – it's very fast to set up, integrates well with LLM frameworks like Langchain and can be extended to meet the use case you describe below. [Vercel](notion://www.notion.so/tidemarkcap/Vercel.com) is the other platform that Diego used for the VKSP
- Applications




I want to a streamlit web app to run ChatGPT across large files and multiple files (using langchain) without cut and paste/ manual steps.

ChatGPT has strong query/ LLM capabilities but can not handle large documents, multiple documents, PDFs, URLs well.

- Get larger files into a workable ChatGPT interface
-example document: https://app.tegus.co/guest/view/tuM7wYVtj1ykx8WEGquBF8UwDS7gVKDXQpuydKV8H75Z6onX5Yn9tWhtiPz8)

- Get different types of files into a workable ChatGPT interface
- URLs
- PDFs
- Google slides
- Google docs
-google drive

- Access multiple files at the same time
- run ChatGPT across [30] different documents (let me know if there's increasing complexity the larger the number is

- Administration
- Have a username and password (and an auto pw reset function)
- ability to save Open AI key
- ability to save prompts
- at the individual level
- perhaps at the team level (as a hack we can use a shared google docs linked to the site )

-as a future project we will start pulling in text from Affinity CRM and Notion.


pincone API key: 68358a06-3931-4458-b131-29e284df630a
openai  API key: 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