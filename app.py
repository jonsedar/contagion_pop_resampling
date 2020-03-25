import streamlit as st

def main():
    st.markdown("## Contagious Coughs & Colds 2019 Commute Calculator")
    st.markdown("""An under-researched, statistical toy** to 
                estimate the 
                probability of encountering someone with a contagious cough or 
                cold during your daily round trip commute into the city.""")

    st.markdown('### A naive population resampling model')

    st.markdown("""The probability $P(X>0)$ of finding at least $1$ case in a 
                group of $N$ people given a background no. of cases $m \gg 1$ 
                in the local city population $M$ is a resample with replacement: """)

    st.sidebar.markdown('## Settings')

    st.sidebar.markdown('### Confirmed Cases')

    m = st.sidebar.slider('Count of confirmed cases (m) in the city', min_value=50, 
                            max_value=200000, value=30000, step=5000)
    M = st.sidebar.slider('Population (M) in the city', min_value=500000, 
                            max_value=20000000, value=8500000, step=500000)

    p = m/M

    st.sidebar.markdown('### Commute Details')

    commute_people_per_min = {'Walk / Cycle': 1.,
                             'Ferry': 4.,
                            'Train / Subway (direct)': 8., 
                            'Train / Subway (1+ change)': 12.}

    commute_method = st.sidebar.radio('Primary Commute Method', 
                            list(commute_people_per_min.keys()), index=2)
    n_commuters = commute_people_per_min[commute_method]

    st.sidebar.markdown(f"""<sub><sup>This method assumes \** aerosol contact 
                ($\Delta \ 2m$) with 
                ${n_commuters:.0f}$ new commuters per min during commute, 
                inc. busy stations, crowded streets etc.</sup></sub>""", 
                unsafe_allow_html=True)

    commute_duration = st.sidebar.slider('Commute Duration (mins)', min_value=15, 
    max_value=120, value=45, step=15)

    N = commute_people_per_min[commute_method] * commute_duration * 2

    st.latex(r'P(X>0) = 1 - (1-p)^{N} = f, \, \text{ ... where } \, p = \frac{m}{M}')

    st.markdown("""$\\Longleftarrow$ _Setup the sliders on the left sidebar (**>**)
                according to your situation_""")

    f = 1 - (1-(p))**N

    st.markdown('#### $\\Longrightarrow$ Results:')

    st.info(f"""Proportion of cases ($m={m:.0f}, M = {M/1e6:.1f}M$): $p = {p*100:.4f}\%$ 
            \nCommuters encountered during a round trip: $N \\approx {N:.0f}$
            \n**Est. prob. of encountering a contagious cough or cold:** $P(X>0) = {f*100:.1f}\%$""")
    
    st.info(f"""... and over a 5 day week: $P(X>0|5 \, days) 
                = 1 - (1-f)^5 = {(1 - (1-f)**5) *100:.1f}\\%$""")

    # st.markdown("""Additional hack for Conference attendance: change the sliders
    #             to generate $p$ appropriate to the sum of the expected attendees' 
    #             home towns / states / countries and set $N$ appropriate to the 
    #             number of conference attendees. Now $P(X>0)$ can help you decide 
    #             whether to attend.""")


    # st.markdown('---')
    st.markdown("""<sub>\** NOTE: This naive model is only to illustrate the power 
                of social separation, and makes no attempt to model 
                case discovery rates / transmission rates or methods or vectors / 
                crowd dynamics / self quarantine etc.
                **Do not use this for anything!**</sub>""",
                unsafe_allow_html=True)



if __name__ == "__main__":
    main()