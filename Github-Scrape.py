{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# github-topics-scrape\n",
    "\n",
    "Outline:\n",
    "- We're going to scrape https://github.com/topics\n",
    "- We'll get a list of topics. For each topic, we'll get topic title, topic page URL and topic description\n",
    "- For each topic, we'll get the top 25 repositories in the topic from the topic page \n",
    "- For each topic we'll create a CSV file in the following format: \n",
    "\n",
    "Repo Name, Username, Stars, Repo URL\n",
    "ex. three.js, mrdoob, 69700, https://github.com/mrdoob/three.js\n",
    "libgdx, libgdx,18300, https://github.com/libgdx/libgdx"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "!pip install requests --upgrade --quiet"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "topics_url = 'https://github.com/topics'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "response = requests.get(topics_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "200"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "response.status_code"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "164738"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(response.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "page_contents = response.text "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'\\n\\n<!DOCTYPE html>\\n<html lang=\"en\" data-color-mode=\"auto\" data-light-theme=\"light\" data-dark-theme=\"dark\"  data-a11y-animated-images=\"system\" data-a11y-link-underlines=\"false\">\\n  <head>\\n    <meta charset=\"utf-8\">\\n  <link rel=\"dns-prefetch\" href=\"https://github.githubassets.com\">\\n  <link rel=\"dns-prefetch\" href=\"https://avatars.githubusercontent.com\">\\n  <link rel=\"dns-prefetch\" href=\"https://github-cloud.s3.amazonaws.com\">\\n  <link rel=\"dns-prefetch\" href=\"https://user-images.githubusercontent.com/\">\\n  <link rel=\"preconnect\" href=\"https://github.githubassets.com\" crossorigin>\\n  <link rel=\"preconnect\" href=\"https://avatars.githubusercontent.com\">\\n\\n  \\n\\n  <link crossorigin=\"anonymous\" media=\"all\" rel=\"stylesheet\" href=\"https://github.githubassets.com/assets/light-8cafbcbd78f4.css\" /><link crossorigin=\"anonymous\" media=\"all\" rel=\"stylesheet\" href=\"https://github.githubassets.com/assets/dark-31dc14e38457.css\" /><link data-color-theme=\"dark_dimmed\" crossorigin=\"anonymous\" media=\"all\" rel=\"style'"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "page_contents[:1000] #looks at first 1000 characters of html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "with open('webpage.html','w') as f: #save html to file \n",
    "    f.write(page_contents)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Use BeautifulSoup to parse and extract information  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "!pip install beautifulsoup4 --upgrade --quiet"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "from bs4 import BeautifulSoup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "doc = BeautifulSoup(page_contents,'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "bs4.BeautifulSoup"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(doc)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "selection_class = 'f3 lh-condensed mb-0 mt-1 Link--primary'\n",
    "\n",
    "topic_title_tags = doc.find_all('p', {'class': selection_class}) #finds topic title tags"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "30"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(topic_title_tags)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<p class=\"f3 lh-condensed mb-0 mt-1 Link--primary\">3D</p>,\n",
       " <p class=\"f3 lh-condensed mb-0 mt-1 Link--primary\">Ajax</p>,\n",
       " <p class=\"f3 lh-condensed mb-0 mt-1 Link--primary\">Algorithm</p>,\n",
       " <p class=\"f3 lh-condensed mb-0 mt-1 Link--primary\">Amp</p>,\n",
       " <p class=\"f3 lh-condensed mb-0 mt-1 Link--primary\">Android</p>,\n",
       " <p class=\"f3 lh-condensed mb-0 mt-1 Link--primary\">Angular</p>,\n",
       " <p class=\"f3 lh-condensed mb-0 mt-1 Link--primary\">Ansible</p>,\n",
       " <p class=\"f3 lh-condensed mb-0 mt-1 Link--primary\">API</p>,\n",
       " <p class=\"f3 lh-condensed mb-0 mt-1 Link--primary\">Arduino</p>,\n",
       " <p class=\"f3 lh-condensed mb-0 mt-1 Link--primary\">ASP.NET</p>,\n",
       " <p class=\"f3 lh-condensed mb-0 mt-1 Link--primary\">Atom</p>,\n",
       " <p class=\"f3 lh-condensed mb-0 mt-1 Link--primary\">Awesome Lists</p>,\n",
       " <p class=\"f3 lh-condensed mb-0 mt-1 Link--primary\">Amazon Web Services</p>,\n",
       " <p class=\"f3 lh-condensed mb-0 mt-1 Link--primary\">Azure</p>,\n",
       " <p class=\"f3 lh-condensed mb-0 mt-1 Link--primary\">Babel</p>,\n",
       " <p class=\"f3 lh-condensed mb-0 mt-1 Link--primary\">Bash</p>,\n",
       " <p class=\"f3 lh-condensed mb-0 mt-1 Link--primary\">Bitcoin</p>,\n",
       " <p class=\"f3 lh-condensed mb-0 mt-1 Link--primary\">Bootstrap</p>,\n",
       " <p class=\"f3 lh-condensed mb-0 mt-1 Link--primary\">Bot</p>,\n",
       " <p class=\"f3 lh-condensed mb-0 mt-1 Link--primary\">C</p>,\n",
       " <p class=\"f3 lh-condensed mb-0 mt-1 Link--primary\">Chrome</p>,\n",
       " <p class=\"f3 lh-condensed mb-0 mt-1 Link--primary\">Chrome extension</p>,\n",
       " <p class=\"f3 lh-condensed mb-0 mt-1 Link--primary\">Command line interface</p>,\n",
       " <p class=\"f3 lh-condensed mb-0 mt-1 Link--primary\">Clojure</p>,\n",
       " <p class=\"f3 lh-condensed mb-0 mt-1 Link--primary\">Code quality</p>,\n",
       " <p class=\"f3 lh-condensed mb-0 mt-1 Link--primary\">Code review</p>,\n",
       " <p class=\"f3 lh-condensed mb-0 mt-1 Link--primary\">Compiler</p>,\n",
       " <p class=\"f3 lh-condensed mb-0 mt-1 Link--primary\">Continuous integration</p>,\n",
       " <p class=\"f3 lh-condensed mb-0 mt-1 Link--primary\">COVID-19</p>,\n",
       " <p class=\"f3 lh-condensed mb-0 mt-1 Link--primary\">C++</p>]"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "topic_title_tags"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "desc_selector = 'f5 color-fg-muted mb-0 mt-1'\n",
    "topic_desc_tags = doc.find_all('p', {'class' : desc_selector}) #finds description"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<p class=\"f5 color-fg-muted mb-0 mt-1\">\n",
       "           3D refers to the use of three-dimensional graphics, modeling, and animation in various industries.\n",
       "         </p>,\n",
       " <p class=\"f5 color-fg-muted mb-0 mt-1\">\n",
       "           Ajax is a technique for creating interactive web applications.\n",
       "         </p>,\n",
       " <p class=\"f5 color-fg-muted mb-0 mt-1\">\n",
       "           Algorithms are self-contained sequences that carry out a variety of tasks.\n",
       "         </p>,\n",
       " <p class=\"f5 color-fg-muted mb-0 mt-1\">\n",
       "           Amp is a non-blocking concurrency library for PHP.\n",
       "         </p>,\n",
       " <p class=\"f5 color-fg-muted mb-0 mt-1\">\n",
       "           Android is an operating system built by Google designed for mobile devices.\n",
       "         </p>,\n",
       " <p class=\"f5 color-fg-muted mb-0 mt-1\">\n",
       "           Angular is an open source web application platform.\n",
       "         </p>,\n",
       " <p class=\"f5 color-fg-muted mb-0 mt-1\">\n",
       "           Ansible is a simple and powerful automation engine.\n",
       "         </p>,\n",
       " <p class=\"f5 color-fg-muted mb-0 mt-1\">\n",
       "           An API (Application Programming Interface) is a collection of protocols and subroutines for building software.\n",
       "         </p>,\n",
       " <p class=\"f5 color-fg-muted mb-0 mt-1\">\n",
       "           Arduino is an open source platform for building electronic devices.\n",
       "         </p>,\n",
       " <p class=\"f5 color-fg-muted mb-0 mt-1\">\n",
       "           ASP.NET is a web framework for building modern web apps and services.\n",
       "         </p>,\n",
       " <p class=\"f5 color-fg-muted mb-0 mt-1\">\n",
       "           Atom is a open source text editor built with web technologies.\n",
       "         </p>,\n",
       " <p class=\"f5 color-fg-muted mb-0 mt-1\">\n",
       "           An awesome list is a list of awesome things curated by the community.\n",
       "         </p>,\n",
       " <p class=\"f5 color-fg-muted mb-0 mt-1\">\n",
       "           Amazon Web Services provides on-demand cloud computing platforms on a subscription basis.\n",
       "         </p>,\n",
       " <p class=\"f5 color-fg-muted mb-0 mt-1\">\n",
       "           Azure is a cloud computing service created by Microsoft.\n",
       "         </p>,\n",
       " <p class=\"f5 color-fg-muted mb-0 mt-1\">\n",
       "           Babel is a compiler for writing next generation JavaScript, today.\n",
       "         </p>,\n",
       " <p class=\"f5 color-fg-muted mb-0 mt-1\">\n",
       "           Bash is a shell and command language interpreter for the GNU operating system.\n",
       "         </p>,\n",
       " <p class=\"f5 color-fg-muted mb-0 mt-1\">\n",
       "           Bitcoin is a cryptocurrency developed by Satoshi Nakamoto.\n",
       "         </p>,\n",
       " <p class=\"f5 color-fg-muted mb-0 mt-1\">\n",
       "           Bootstrap is an HTML, CSS, and JavaScript framework.\n",
       "         </p>,\n",
       " <p class=\"f5 color-fg-muted mb-0 mt-1\">\n",
       "           A bot is an application that runs automated tasks over the Internet.\n",
       "         </p>,\n",
       " <p class=\"f5 color-fg-muted mb-0 mt-1\">\n",
       "           C is a general purpose programming language that first appeared in 1972.\n",
       "         </p>,\n",
       " <p class=\"f5 color-fg-muted mb-0 mt-1\">\n",
       "           Chrome is a web browser from the tech company Google.\n",
       "         </p>,\n",
       " <p class=\"f5 color-fg-muted mb-0 mt-1\">\n",
       "           Chrome extensions enable users to customize the Chrome browsing experience.\n",
       "         </p>,\n",
       " <p class=\"f5 color-fg-muted mb-0 mt-1\">\n",
       "           A CLI, or command-line interface, is a console that helps users issue commands to a program.\n",
       "         </p>,\n",
       " <p class=\"f5 color-fg-muted mb-0 mt-1\">\n",
       "           Clojure is a dynamic, general-purpose programming language.\n",
       "         </p>,\n",
       " <p class=\"f5 color-fg-muted mb-0 mt-1\">\n",
       "           Automate your code review with style, quality, security, and test‑coverage checks when you need them.\n",
       "         </p>,\n",
       " <p class=\"f5 color-fg-muted mb-0 mt-1\">\n",
       "           Ensure your code meets quality standards and ship with confidence.\n",
       "         </p>,\n",
       " <p class=\"f5 color-fg-muted mb-0 mt-1\">\n",
       "           Compilers are software that translate higher-level programming languages to lower-level languages (e.g. machine code).\n",
       "         </p>,\n",
       " <p class=\"f5 color-fg-muted mb-0 mt-1\">\n",
       "           Automatically build and test your code as you push it upstream, preventing bugs from being deployed to production.\n",
       "         </p>,\n",
       " <p class=\"f5 color-fg-muted mb-0 mt-1\">\n",
       "           The coronavirus disease 2019 (COVID-19) is an infectious disease caused by SARS-CoV-2.\n",
       "         </p>,\n",
       " <p class=\"f5 color-fg-muted mb-0 mt-1\">\n",
       "           C++ is a general purpose and object-oriented programming language.\n",
       "         </p>]"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "topic_desc_tags"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "topic_title_tag0 = topic_title_tags[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "topic_link_tags = doc.find_all('a', {'class': 'no-underline flex-1 d-flex flex-column'}) #finds topic link "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "30"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(topic_link_tags)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://github.com/topics/3d\n"
     ]
    }
   ],
   "source": [
    "topic0_url = \"https://github.com\" + topic_link_tags[0]['href']\n",
    "print(topic0_url)  #finds href and appends to github to build link "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['3D', 'Ajax', 'Algorithm', 'Amp', 'Android', 'Angular', 'Ansible', 'API', 'Arduino', 'ASP.NET', 'Atom', 'Awesome Lists', 'Amazon Web Services', 'Azure', 'Babel', 'Bash', 'Bitcoin', 'Bootstrap', 'Bot', 'C', 'Chrome', 'Chrome extension', 'Command line interface', 'Clojure', 'Code quality', 'Code review', 'Compiler', 'Continuous integration', 'COVID-19', 'C++']\n"
     ]
    }
   ],
   "source": [
    "topic_titles = [] # [] = empty dictionary \n",
    "\n",
    "for tag in topic_title_tags:\n",
    "    topic_titles.append(tag.text)\n",
    "\n",
    "print(topic_titles) # grabs and shows all topic title tags "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['3D refers to the use of three-dimensional graphics, modeling, and animation in various industries.', 'Ajax is a technique for creating interactive web applications.', 'Algorithms are self-contained sequences that carry out a variety of tasks.', 'Amp is a non-blocking concurrency library for PHP.', 'Android is an operating system built by Google designed for mobile devices.', 'Angular is an open source web application platform.', 'Ansible is a simple and powerful automation engine.', 'An API (Application Programming Interface) is a collection of protocols and subroutines for building software.', 'Arduino is an open source platform for building electronic devices.', 'ASP.NET is a web framework for building modern web apps and services.', 'Atom is a open source text editor built with web technologies.', 'An awesome list is a list of awesome things curated by the community.', 'Amazon Web Services provides on-demand cloud computing platforms on a subscription basis.', 'Azure is a cloud computing service created by Microsoft.', 'Babel is a compiler for writing next generation JavaScript, today.', 'Bash is a shell and command language interpreter for the GNU operating system.', 'Bitcoin is a cryptocurrency developed by Satoshi Nakamoto.', 'Bootstrap is an HTML, CSS, and JavaScript framework.', 'A bot is an application that runs automated tasks over the Internet.', 'C is a general purpose programming language that first appeared in 1972.', 'Chrome is a web browser from the tech company Google.', 'Chrome extensions enable users to customize the Chrome browsing experience.', 'A CLI, or command-line interface, is a console that helps users issue commands to a program.', 'Clojure is a dynamic, general-purpose programming language.', 'Automate your code review with style, quality, security, and test‑coverage checks when you need them.', 'Ensure your code meets quality standards and ship with confidence.', 'Compilers are software that translate higher-level programming languages to lower-level languages (e.g. machine code).', 'Automatically build and test your code as you push it upstream, preventing bugs from being deployed to production.', 'The coronavirus disease 2019 (COVID-19) is an infectious disease caused by SARS-CoV-2.', 'C++ is a general purpose and object-oriented programming language.']\n"
     ]
    }
   ],
   "source": [
    "topic_descs = []\n",
    "\n",
    "for tag in topic_desc_tags:\n",
    "    topic_descs.append(tag.text.strip()) #strips empty space before and after text \n",
    "    \n",
    "print(topic_descs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['https://github.com/topics/3d',\n",
       " 'https://github.com/topics/ajax',\n",
       " 'https://github.com/topics/algorithm',\n",
       " 'https://github.com/topics/amphp',\n",
       " 'https://github.com/topics/android',\n",
       " 'https://github.com/topics/angular',\n",
       " 'https://github.com/topics/ansible',\n",
       " 'https://github.com/topics/api',\n",
       " 'https://github.com/topics/arduino',\n",
       " 'https://github.com/topics/aspnet',\n",
       " 'https://github.com/topics/atom',\n",
       " 'https://github.com/topics/awesome',\n",
       " 'https://github.com/topics/aws',\n",
       " 'https://github.com/topics/azure',\n",
       " 'https://github.com/topics/babel',\n",
       " 'https://github.com/topics/bash',\n",
       " 'https://github.com/topics/bitcoin',\n",
       " 'https://github.com/topics/bootstrap',\n",
       " 'https://github.com/topics/bot',\n",
       " 'https://github.com/topics/c',\n",
       " 'https://github.com/topics/chrome',\n",
       " 'https://github.com/topics/chrome-extension',\n",
       " 'https://github.com/topics/cli',\n",
       " 'https://github.com/topics/clojure',\n",
       " 'https://github.com/topics/code-quality',\n",
       " 'https://github.com/topics/code-review',\n",
       " 'https://github.com/topics/compiler',\n",
       " 'https://github.com/topics/continuous-integration',\n",
       " 'https://github.com/topics/covid-19',\n",
       " 'https://github.com/topics/cpp']"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "topic_urls = []\n",
    "base_url = 'https://github.com'\n",
    "\n",
    "for tag in topic_link_tags:\n",
    "    topic_urls.append(base_url + tag['href'])\n",
    "    \n",
    "topic_urls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pandas in /opt/conda/lib/python3.9/site-packages (1.3.4)\r\n",
      "Requirement already satisfied: python-dateutil>=2.7.3 in /opt/conda/lib/python3.9/site-packages (from pandas) (2.8.2)\r\n",
      "Requirement already satisfied: pytz>=2017.3 in /opt/conda/lib/python3.9/site-packages (from pandas) (2021.3)\r\n",
      "Requirement already satisfied: numpy>=1.17.3 in /opt/conda/lib/python3.9/site-packages (from pandas) (1.20.3)\r\n",
      "Requirement already satisfied: six>=1.5 in /opt/conda/lib/python3.9/site-packages (from python-dateutil>=2.7.3->pandas) (1.16.0)\r\n"
     ]
    }
   ],
   "source": [
    "!pip install pandas --quiet"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [],
   "source": [
    "topics_dict = {\n",
    "    'title' : topic_titles,\n",
    "    'description' : topic_descs,\n",
    "    'url' : topic_urls\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [],
   "source": [
    "topics_df = pd.DataFrame(topics_dict)  #create dataframe and name it topic_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>title</th>\n",
       "      <th>description</th>\n",
       "      <th>url</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>3D</td>\n",
       "      <td>3D refers to the use of three-dimensional grap...</td>\n",
       "      <td>https://github.com/topics/3d</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Ajax</td>\n",
       "      <td>Ajax is a technique for creating interactive w...</td>\n",
       "      <td>https://github.com/topics/ajax</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Algorithm</td>\n",
       "      <td>Algorithms are self-contained sequences that c...</td>\n",
       "      <td>https://github.com/topics/algorithm</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Amp</td>\n",
       "      <td>Amp is a non-blocking concurrency library for ...</td>\n",
       "      <td>https://github.com/topics/amphp</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Android</td>\n",
       "      <td>Android is an operating system built by Google...</td>\n",
       "      <td>https://github.com/topics/android</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Angular</td>\n",
       "      <td>Angular is an open source web application plat...</td>\n",
       "      <td>https://github.com/topics/angular</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Ansible</td>\n",
       "      <td>Ansible is a simple and powerful automation en...</td>\n",
       "      <td>https://github.com/topics/ansible</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>API</td>\n",
       "      <td>An API (Application Programming Interface) is ...</td>\n",
       "      <td>https://github.com/topics/api</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Arduino</td>\n",
       "      <td>Arduino is an open source platform for buildin...</td>\n",
       "      <td>https://github.com/topics/arduino</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>ASP.NET</td>\n",
       "      <td>ASP.NET is a web framework for building modern...</td>\n",
       "      <td>https://github.com/topics/aspnet</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>Atom</td>\n",
       "      <td>Atom is a open source text editor built with w...</td>\n",
       "      <td>https://github.com/topics/atom</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>Awesome Lists</td>\n",
       "      <td>An awesome list is a list of awesome things cu...</td>\n",
       "      <td>https://github.com/topics/awesome</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>Amazon Web Services</td>\n",
       "      <td>Amazon Web Services provides on-demand cloud c...</td>\n",
       "      <td>https://github.com/topics/aws</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>Azure</td>\n",
       "      <td>Azure is a cloud computing service created by ...</td>\n",
       "      <td>https://github.com/topics/azure</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>Babel</td>\n",
       "      <td>Babel is a compiler for writing next generatio...</td>\n",
       "      <td>https://github.com/topics/babel</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>Bash</td>\n",
       "      <td>Bash is a shell and command language interpret...</td>\n",
       "      <td>https://github.com/topics/bash</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>Bitcoin</td>\n",
       "      <td>Bitcoin is a cryptocurrency developed by Satos...</td>\n",
       "      <td>https://github.com/topics/bitcoin</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>Bootstrap</td>\n",
       "      <td>Bootstrap is an HTML, CSS, and JavaScript fram...</td>\n",
       "      <td>https://github.com/topics/bootstrap</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>Bot</td>\n",
       "      <td>A bot is an application that runs automated ta...</td>\n",
       "      <td>https://github.com/topics/bot</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>C</td>\n",
       "      <td>C is a general purpose programming language th...</td>\n",
       "      <td>https://github.com/topics/c</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>Chrome</td>\n",
       "      <td>Chrome is a web browser from the tech company ...</td>\n",
       "      <td>https://github.com/topics/chrome</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>Chrome extension</td>\n",
       "      <td>Chrome extensions enable users to customize th...</td>\n",
       "      <td>https://github.com/topics/chrome-extension</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>Command line interface</td>\n",
       "      <td>A CLI, or command-line interface, is a console...</td>\n",
       "      <td>https://github.com/topics/cli</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>Clojure</td>\n",
       "      <td>Clojure is a dynamic, general-purpose programm...</td>\n",
       "      <td>https://github.com/topics/clojure</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>Code quality</td>\n",
       "      <td>Automate your code review with style, quality,...</td>\n",
       "      <td>https://github.com/topics/code-quality</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>Code review</td>\n",
       "      <td>Ensure your code meets quality standards and s...</td>\n",
       "      <td>https://github.com/topics/code-review</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>26</th>\n",
       "      <td>Compiler</td>\n",
       "      <td>Compilers are software that translate higher-l...</td>\n",
       "      <td>https://github.com/topics/compiler</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>27</th>\n",
       "      <td>Continuous integration</td>\n",
       "      <td>Automatically build and test your code as you ...</td>\n",
       "      <td>https://github.com/topics/continuous-integration</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>COVID-19</td>\n",
       "      <td>The coronavirus disease 2019 (COVID-19) is an ...</td>\n",
       "      <td>https://github.com/topics/covid-19</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>29</th>\n",
       "      <td>C++</td>\n",
       "      <td>C++ is a general purpose and object-oriented p...</td>\n",
       "      <td>https://github.com/topics/cpp</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                     title                                        description  \\\n",
       "0                       3D  3D refers to the use of three-dimensional grap...   \n",
       "1                     Ajax  Ajax is a technique for creating interactive w...   \n",
       "2                Algorithm  Algorithms are self-contained sequences that c...   \n",
       "3                      Amp  Amp is a non-blocking concurrency library for ...   \n",
       "4                  Android  Android is an operating system built by Google...   \n",
       "5                  Angular  Angular is an open source web application plat...   \n",
       "6                  Ansible  Ansible is a simple and powerful automation en...   \n",
       "7                      API  An API (Application Programming Interface) is ...   \n",
       "8                  Arduino  Arduino is an open source platform for buildin...   \n",
       "9                  ASP.NET  ASP.NET is a web framework for building modern...   \n",
       "10                    Atom  Atom is a open source text editor built with w...   \n",
       "11           Awesome Lists  An awesome list is a list of awesome things cu...   \n",
       "12     Amazon Web Services  Amazon Web Services provides on-demand cloud c...   \n",
       "13                   Azure  Azure is a cloud computing service created by ...   \n",
       "14                   Babel  Babel is a compiler for writing next generatio...   \n",
       "15                    Bash  Bash is a shell and command language interpret...   \n",
       "16                 Bitcoin  Bitcoin is a cryptocurrency developed by Satos...   \n",
       "17               Bootstrap  Bootstrap is an HTML, CSS, and JavaScript fram...   \n",
       "18                     Bot  A bot is an application that runs automated ta...   \n",
       "19                       C  C is a general purpose programming language th...   \n",
       "20                  Chrome  Chrome is a web browser from the tech company ...   \n",
       "21        Chrome extension  Chrome extensions enable users to customize th...   \n",
       "22  Command line interface  A CLI, or command-line interface, is a console...   \n",
       "23                 Clojure  Clojure is a dynamic, general-purpose programm...   \n",
       "24            Code quality  Automate your code review with style, quality,...   \n",
       "25             Code review  Ensure your code meets quality standards and s...   \n",
       "26                Compiler  Compilers are software that translate higher-l...   \n",
       "27  Continuous integration  Automatically build and test your code as you ...   \n",
       "28                COVID-19  The coronavirus disease 2019 (COVID-19) is an ...   \n",
       "29                     C++  C++ is a general purpose and object-oriented p...   \n",
       "\n",
       "                                                 url  \n",
       "0                       https://github.com/topics/3d  \n",
       "1                     https://github.com/topics/ajax  \n",
       "2                https://github.com/topics/algorithm  \n",
       "3                    https://github.com/topics/amphp  \n",
       "4                  https://github.com/topics/android  \n",
       "5                  https://github.com/topics/angular  \n",
       "6                  https://github.com/topics/ansible  \n",
       "7                      https://github.com/topics/api  \n",
       "8                  https://github.com/topics/arduino  \n",
       "9                   https://github.com/topics/aspnet  \n",
       "10                    https://github.com/topics/atom  \n",
       "11                 https://github.com/topics/awesome  \n",
       "12                     https://github.com/topics/aws  \n",
       "13                   https://github.com/topics/azure  \n",
       "14                   https://github.com/topics/babel  \n",
       "15                    https://github.com/topics/bash  \n",
       "16                 https://github.com/topics/bitcoin  \n",
       "17               https://github.com/topics/bootstrap  \n",
       "18                     https://github.com/topics/bot  \n",
       "19                       https://github.com/topics/c  \n",
       "20                  https://github.com/topics/chrome  \n",
       "21        https://github.com/topics/chrome-extension  \n",
       "22                     https://github.com/topics/cli  \n",
       "23                 https://github.com/topics/clojure  \n",
       "24            https://github.com/topics/code-quality  \n",
       "25             https://github.com/topics/code-review  \n",
       "26                https://github.com/topics/compiler  \n",
       "27  https://github.com/topics/continuous-integration  \n",
       "28                https://github.com/topics/covid-19  \n",
       "29                     https://github.com/topics/cpp  "
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "topics_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Creats CSV file(s) with the extracted information"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [],
   "source": [
    "topics_df.to_csv('topics.csv', index = None)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Getting information out of topic page"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [],
   "source": [
    "topic_page_url = topic_urls[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://github.com/topics/3d'"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "topic_page_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [],
   "source": [
    "response = requests.get(topic_page_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "200"
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "response.status_code"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "476394"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(response.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [],
   "source": [
    "topic_doc = BeautifulSoup(response.text, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [],
   "source": [
    "h3_selection_class = 'f3 color-fg-muted text-normal lh-condensed'\n",
    "repo_tags = topic_doc.find_all('h3', {'class' : h3_selection_class})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "20"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(repo_tags)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [],
   "source": [
    "a_tags = repo_tags[0].find_all('a')  # check first repo tag"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<a class=\"Link\" data-hydro-click='{\"event_type\":\"explore.click\",\"payload\":{\"click_context\":\"REPOSITORY_CARD\",\"click_target\":\"OWNER\",\"click_visual_representation\":\"REPOSITORY_OWNER_HEADING\",\"actor_id\":null,\"record_id\":97088,\"originating_url\":\"https://github.com/topics/3d\",\"user_id\":null}}' data-hydro-click-hmac=\"4bdbc49d3c05ae7f70b531fbce709a384200b0768554e0172950286a8db30940\" data-turbo=\"false\" data-view-component=\"true\" href=\"/mrdoob\">\n",
       "             mrdoob\n",
       " </a>,\n",
       " <a class=\"Link text-bold wb-break-word\" data-hydro-click='{\"event_type\":\"explore.click\",\"payload\":{\"click_context\":\"REPOSITORY_CARD\",\"click_target\":\"REPOSITORY\",\"click_visual_representation\":\"REPOSITORY_NAME_HEADING\",\"actor_id\":null,\"record_id\":576201,\"originating_url\":\"https://github.com/topics/3d\",\"user_id\":null}}' data-hydro-click-hmac=\"517d3d5cb9d89752156923904a4238816bc9b51ab7772f3e3644ce897d8dd4e5\" data-turbo=\"false\" data-view-component=\"true\" href=\"/mrdoob/three.js\">\n",
       "             three.js\n",
       " </a>]"
      ]
     },
     "execution_count": 95,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a_tags"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'mrdoob'"
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    " a_tags[0].text.strip()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'three.js'"
      ]
     },
     "execution_count": 99,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a_tags[1].text.strip()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://github.com/mrdoob/three.js\n"
     ]
    }
   ],
   "source": [
    "base_url = 'https://github.com'\n",
    "repo_url = base_url + a_tags[1]['href']\n",
    "print(repo_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [],
   "source": [
    "star_tags = topic_doc.find_all('span', {'class': 'Counter js-social-count'})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "20"
      ]
     },
     "execution_count": 106,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(star_tags)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'93.7k'"
      ]
     },
     "execution_count": 108,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "star_tags[0].text.strip()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {},
   "outputs": [],
   "source": [
    "def parse_star_count(stars_str):\n",
    "    stars_str = stars_str.strip()\n",
    "    if stars_str[-1] == 'k':\n",
    "         return int(float(stars_str[:-1]) *1000)\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "93700"
      ]
     },
     "execution_count": 120,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "parse_star_count(star_tags[0].text.strip())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_repo_info(h3_tag, star_tag): \n",
    "    #returns all the required info about a repository\n",
    "    a_tags = h3_tag.find_all('a')\n",
    "    username = a_tags[0].text.strip()\n",
    "    repo_name = a_tags[1].text.strip()\n",
    "    repo_url = base_url + a_tags[1]['href']\n",
    "    stars = parse_star_count(star_tag.text.strip())\n",
    "    return username, repo_name, stars, repo_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('mrdoob', 'three.js', 93700, 'https://github.com/mrdoob/three.js')"
      ]
     },
     "execution_count": 123,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "get_repo_info(repo_tags[0],star_tags[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "metadata": {},
   "outputs": [],
   "source": [
    "topic_repos_dict = {\n",
    "    'username' : [],\n",
    "    'repo_name' : [],\n",
    "    'stars' : [],\n",
    "    'repo_url' : []\n",
    "}\n",
    "\n",
    "for i in range(len(repo_tags)):\n",
    "    repo_info = get_repo_info(repo_tags[i], star_tags[i])\n",
    "    topic_repos_dict['username'].append(repo_info[0])\n",
    "    topic_repos_dict['repo_name'].append(repo_info[1])\n",
    "    topic_repos_dict['stars'].append(repo_info[2])\n",
    "    topic_repos_dict['repo_url'].append(repo_info[3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'username': ['mrdoob',\n",
       "  'pmndrs',\n",
       "  'libgdx',\n",
       "  'BabylonJS',\n",
       "  'ssloy',\n",
       "  'lettier',\n",
       "  'aframevr',\n",
       "  'FreeCAD',\n",
       "  'CesiumGS',\n",
       "  'metafizzy',\n",
       "  'isl-org',\n",
       "  'blender',\n",
       "  'timzhang642',\n",
       "  'a1studmuffin',\n",
       "  'domlysz',\n",
       "  'FyroxEngine',\n",
       "  'nerfstudio-project',\n",
       "  'google',\n",
       "  'openscad',\n",
       "  'spritejs'],\n",
       " 'repo_name': ['three.js',\n",
       "  'react-three-fiber',\n",
       "  'libgdx',\n",
       "  'Babylon.js',\n",
       "  'tinyrenderer',\n",
       "  '3d-game-shaders-for-beginners',\n",
       "  'aframe',\n",
       "  'FreeCAD',\n",
       "  'cesium',\n",
       "  'zdog',\n",
       "  'Open3D',\n",
       "  'blender',\n",
       "  '3D-Machine-Learning',\n",
       "  'SpaceshipGenerator',\n",
       "  'BlenderGIS',\n",
       "  'Fyrox',\n",
       "  'nerfstudio',\n",
       "  'model-viewer',\n",
       "  'openscad',\n",
       "  'spritejs'],\n",
       " 'stars': [93700,\n",
       "  23500,\n",
       "  21800,\n",
       "  21100,\n",
       "  17600,\n",
       "  15900,\n",
       "  15600,\n",
       "  14800,\n",
       "  10800,\n",
       "  10000,\n",
       "  9300,\n",
       "  9100,\n",
       "  9000,\n",
       "  7400,\n",
       "  6600,\n",
       "  6400,\n",
       "  6200,\n",
       "  5800,\n",
       "  5800,\n",
       "  5200],\n",
       " 'repo_url': ['https://github.com/mrdoob/three.js',\n",
       "  'https://github.com/pmndrs/react-three-fiber',\n",
       "  'https://github.com/libgdx/libgdx',\n",
       "  'https://github.com/BabylonJS/Babylon.js',\n",
       "  'https://github.com/ssloy/tinyrenderer',\n",
       "  'https://github.com/lettier/3d-game-shaders-for-beginners',\n",
       "  'https://github.com/aframevr/aframe',\n",
       "  'https://github.com/FreeCAD/FreeCAD',\n",
       "  'https://github.com/CesiumGS/cesium',\n",
       "  'https://github.com/metafizzy/zdog',\n",
       "  'https://github.com/isl-org/Open3D',\n",
       "  'https://github.com/blender/blender',\n",
       "  'https://github.com/timzhang642/3D-Machine-Learning',\n",
       "  'https://github.com/a1studmuffin/SpaceshipGenerator',\n",
       "  'https://github.com/domlysz/BlenderGIS',\n",
       "  'https://github.com/FyroxEngine/Fyrox',\n",
       "  'https://github.com/nerfstudio-project/nerfstudio',\n",
       "  'https://github.com/google/model-viewer',\n",
       "  'https://github.com/openscad/openscad',\n",
       "  'https://github.com/spritejs/spritejs']}"
      ]
     },
     "execution_count": 134,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "topic_repos_dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 166,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_topic_page(topic_url):\n",
    "    # Download the page\n",
    "    response = requests.get(topic_page_url)\n",
    "    # Check successful response\n",
    "    if response.status_code != 200:\n",
    "        raise Exception('Failed to load page{}'.format(topic_url))\n",
    "    # Parse using beautiful soup    \n",
    "    topic_doc = BeautifulSoup(response.text, 'html.parser')\n",
    "    return topic_doc\n",
    "   \n",
    "def get_repo_info(h3_tag, star_tag): \n",
    "    #returns all the required info about a repository\n",
    "    a_tags = h3_tag.find_all('a')\n",
    "    username = a_tags[0].text.strip()\n",
    "    repo_name = a_tags[1].text.strip()\n",
    "    repo_url = base_url + a_tags[1]['href']\n",
    "    stars = parse_star_count(star_tag.text.strip())\n",
    "    return username, repo_name, stars, repo_url\n",
    "\n",
    "def get_topic_repos(topic_doc):\n",
    "     # Get h3 tags containing repo title, repo URL, and username\n",
    "    h3_selection_class = 'f3 color-fg-muted text-normal lh-condensed'\n",
    "    repo_tags = topic_doc.find_all('h3', {'class' : h3_selection_class} )\n",
    "    # Get star tags\n",
    "    star_tags = topic_doc.find_all('span', {'class': 'Counter js-social-count'})\n",
    "    \n",
    "    topic_repos_dict = {\n",
    "        'username' : [],\n",
    "        'repo_name' : [],\n",
    "        'stars' : [],\n",
    "        'repo_url' : []\n",
    "    }\n",
    "\n",
    "    # Get repo info\n",
    "    for i in range(len(repo_tags)):\n",
    "        repo_info = get_repo_info(repo_tags[i], star_tags[i])\n",
    "        topic_repos_dict['username'].append(repo_info[0])\n",
    "        topic_repos_dict['repo_name'].append(repo_info[1])\n",
    "        topic_repos_dict['stars'].append(repo_info[2])\n",
    "        topic_repos_dict['repo_url'].append(repo_info[3])\n",
    "        \n",
    "    return pd.DataFrame(topic_repos_dict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 168,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>username</th>\n",
       "      <th>repo_name</th>\n",
       "      <th>stars</th>\n",
       "      <th>repo_url</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>mrdoob</td>\n",
       "      <td>three.js</td>\n",
       "      <td>93700</td>\n",
       "      <td>https://github.com/mrdoob/three.js</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>pmndrs</td>\n",
       "      <td>react-three-fiber</td>\n",
       "      <td>23500</td>\n",
       "      <td>https://github.com/pmndrs/react-three-fiber</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>libgdx</td>\n",
       "      <td>libgdx</td>\n",
       "      <td>21800</td>\n",
       "      <td>https://github.com/libgdx/libgdx</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>BabylonJS</td>\n",
       "      <td>Babylon.js</td>\n",
       "      <td>21100</td>\n",
       "      <td>https://github.com/BabylonJS/Babylon.js</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>ssloy</td>\n",
       "      <td>tinyrenderer</td>\n",
       "      <td>17600</td>\n",
       "      <td>https://github.com/ssloy/tinyrenderer</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>lettier</td>\n",
       "      <td>3d-game-shaders-for-beginners</td>\n",
       "      <td>15900</td>\n",
       "      <td>https://github.com/lettier/3d-game-shaders-for...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>aframevr</td>\n",
       "      <td>aframe</td>\n",
       "      <td>15600</td>\n",
       "      <td>https://github.com/aframevr/aframe</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>FreeCAD</td>\n",
       "      <td>FreeCAD</td>\n",
       "      <td>14800</td>\n",
       "      <td>https://github.com/FreeCAD/FreeCAD</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>CesiumGS</td>\n",
       "      <td>cesium</td>\n",
       "      <td>10800</td>\n",
       "      <td>https://github.com/CesiumGS/cesium</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>metafizzy</td>\n",
       "      <td>zdog</td>\n",
       "      <td>10000</td>\n",
       "      <td>https://github.com/metafizzy/zdog</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>isl-org</td>\n",
       "      <td>Open3D</td>\n",
       "      <td>9300</td>\n",
       "      <td>https://github.com/isl-org/Open3D</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>blender</td>\n",
       "      <td>blender</td>\n",
       "      <td>9100</td>\n",
       "      <td>https://github.com/blender/blender</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>timzhang642</td>\n",
       "      <td>3D-Machine-Learning</td>\n",
       "      <td>9000</td>\n",
       "      <td>https://github.com/timzhang642/3D-Machine-Lear...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>a1studmuffin</td>\n",
       "      <td>SpaceshipGenerator</td>\n",
       "      <td>7400</td>\n",
       "      <td>https://github.com/a1studmuffin/SpaceshipGener...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>domlysz</td>\n",
       "      <td>BlenderGIS</td>\n",
       "      <td>6600</td>\n",
       "      <td>https://github.com/domlysz/BlenderGIS</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>FyroxEngine</td>\n",
       "      <td>Fyrox</td>\n",
       "      <td>6400</td>\n",
       "      <td>https://github.com/FyroxEngine/Fyrox</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>nerfstudio-project</td>\n",
       "      <td>nerfstudio</td>\n",
       "      <td>6200</td>\n",
       "      <td>https://github.com/nerfstudio-project/nerfstudio</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>google</td>\n",
       "      <td>model-viewer</td>\n",
       "      <td>5800</td>\n",
       "      <td>https://github.com/google/model-viewer</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>openscad</td>\n",
       "      <td>openscad</td>\n",
       "      <td>5800</td>\n",
       "      <td>https://github.com/openscad/openscad</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>spritejs</td>\n",
       "      <td>spritejs</td>\n",
       "      <td>5200</td>\n",
       "      <td>https://github.com/spritejs/spritejs</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              username                      repo_name  stars  \\\n",
       "0               mrdoob                       three.js  93700   \n",
       "1               pmndrs              react-three-fiber  23500   \n",
       "2               libgdx                         libgdx  21800   \n",
       "3            BabylonJS                     Babylon.js  21100   \n",
       "4                ssloy                   tinyrenderer  17600   \n",
       "5              lettier  3d-game-shaders-for-beginners  15900   \n",
       "6             aframevr                         aframe  15600   \n",
       "7              FreeCAD                        FreeCAD  14800   \n",
       "8             CesiumGS                         cesium  10800   \n",
       "9            metafizzy                           zdog  10000   \n",
       "10             isl-org                         Open3D   9300   \n",
       "11             blender                        blender   9100   \n",
       "12         timzhang642            3D-Machine-Learning   9000   \n",
       "13        a1studmuffin             SpaceshipGenerator   7400   \n",
       "14             domlysz                     BlenderGIS   6600   \n",
       "15         FyroxEngine                          Fyrox   6400   \n",
       "16  nerfstudio-project                     nerfstudio   6200   \n",
       "17              google                   model-viewer   5800   \n",
       "18            openscad                       openscad   5800   \n",
       "19            spritejs                       spritejs   5200   \n",
       "\n",
       "                                             repo_url  \n",
       "0                  https://github.com/mrdoob/three.js  \n",
       "1         https://github.com/pmndrs/react-three-fiber  \n",
       "2                    https://github.com/libgdx/libgdx  \n",
       "3             https://github.com/BabylonJS/Babylon.js  \n",
       "4               https://github.com/ssloy/tinyrenderer  \n",
       "5   https://github.com/lettier/3d-game-shaders-for...  \n",
       "6                  https://github.com/aframevr/aframe  \n",
       "7                  https://github.com/FreeCAD/FreeCAD  \n",
       "8                  https://github.com/CesiumGS/cesium  \n",
       "9                   https://github.com/metafizzy/zdog  \n",
       "10                  https://github.com/isl-org/Open3D  \n",
       "11                 https://github.com/blender/blender  \n",
       "12  https://github.com/timzhang642/3D-Machine-Lear...  \n",
       "13  https://github.com/a1studmuffin/SpaceshipGener...  \n",
       "14              https://github.com/domlysz/BlenderGIS  \n",
       "15               https://github.com/FyroxEngine/Fyrox  \n",
       "16   https://github.com/nerfstudio-project/nerfstudio  \n",
       "17             https://github.com/google/model-viewer  \n",
       "18               https://github.com/openscad/openscad  \n",
       "19               https://github.com/spritejs/spritejs  "
      ]
     },
     "execution_count": 168,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "get_topic_repos(get_topic_page(topic_urls[5]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 160,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['https://github.com/topics/3d',\n",
       " 'https://github.com/topics/ajax',\n",
       " 'https://github.com/topics/algorithm',\n",
       " 'https://github.com/topics/amphp',\n",
       " 'https://github.com/topics/android',\n",
       " 'https://github.com/topics/angular',\n",
       " 'https://github.com/topics/ansible',\n",
       " 'https://github.com/topics/api',\n",
       " 'https://github.com/topics/arduino',\n",
       " 'https://github.com/topics/aspnet',\n",
       " 'https://github.com/topics/atom',\n",
       " 'https://github.com/topics/awesome',\n",
       " 'https://github.com/topics/aws',\n",
       " 'https://github.com/topics/azure',\n",
       " 'https://github.com/topics/babel',\n",
       " 'https://github.com/topics/bash',\n",
       " 'https://github.com/topics/bitcoin',\n",
       " 'https://github.com/topics/bootstrap',\n",
       " 'https://github.com/topics/bot',\n",
       " 'https://github.com/topics/c',\n",
       " 'https://github.com/topics/chrome',\n",
       " 'https://github.com/topics/chrome-extension',\n",
       " 'https://github.com/topics/cli',\n",
       " 'https://github.com/topics/clojure',\n",
       " 'https://github.com/topics/code-quality',\n",
       " 'https://github.com/topics/code-review',\n",
       " 'https://github.com/topics/compiler',\n",
       " 'https://github.com/topics/continuous-integration',\n",
       " 'https://github.com/topics/covid-19',\n",
       " 'https://github.com/topics/cpp']"
      ]
     },
     "execution_count": 160,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "topic_urls"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Final\n",
    "\n",
    " Write a single function to:\n",
    "\n",
    "1. Get the list of topics from the topics page\n",
    "2. Get the list of top repos from the individual topic page\n",
    "3. For each topic, create a CSV of the top repos for the topic "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def scrape_topic_repos():\n",
    "    topics_ur; = 'https://github.com/topics'"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}