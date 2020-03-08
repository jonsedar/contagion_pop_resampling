import streamlit as st

def main():
    st.markdown("# Contagious Coughs & Colds 2019 Commute Calculator")
    st.markdown("""An under-researched statistical toy \** to 
                estimate the 
                probability of encountering someone with a contagious cough or 
                cold during your daily round trip commute into the city.""")

    st.markdown('### A naive population resampling model')

    st.markdown("""The probability $P(X>0)$ of a finding at least $1$ case in a 
                group of $N$ people given a background no. of cases $m >> 1$ 
                in the local city population $M$ is a resample with replacement: """)

    st.sidebar.markdown('## Settings')

    st.sidebar.markdown('### Confirmed Cases')

    m = st.sidebar.slider('Count of live cases (m) in the city', min_value=10, 
                            max_value=5000, value=100, step=50)
    M = st.sidebar.slider('Population in the city (M)', min_value=500000, 
                            max_value=20000000, value=8500000, step=500000)

    p = m/M
    #st.sidebar.markdown(f'Cases in population $p = {p*100:.3f}\%$')

    st.sidebar.markdown('### Commute Details')

    commute_people_per_min = {'Walk / Cycle': 1.,
                             'Ferry': 4.,
                            'Train / Subway (direct)': 8., 
                            'Train / Subway (1+ change)': 12.}

    commute_method = st.sidebar.radio('Commute Method', 
                            list(commute_people_per_min.keys()), index=2)
    n_commuters = commute_people_per_min[commute_method]

    st.sidebar.markdown(f"""<sub><sup>This method assumes aerosol contact ($\Delta \ 2m$) with 
                ${n_commuters:.0f}$ new commuters per min during commute, 
                inc. busy stations, crowded streets etc.</sup></sub>""", 
                unsafe_allow_html=True)

    commute_duration = st.sidebar.slider('Commute Duration (mins)', min_value=15, 
    max_value=120, value=45, step=15)

    N = commute_people_per_min[commute_method] * commute_duration * 2

    # st.sidebar.markdown(f'$N \\approx$ {N:.0f} commuters encountered during ' + 
    #                     'a round trip commute')

    #st.sidebar.markdown("Now view your $P(X>0) \\Longrightarrow$")


    st.latex(r'P(X>0) = 1 - (1-p)^{N} = f, \, \text{ ... where } \, p = \frac{m}{M}')

    st.markdown("""$\\Longleftarrow$ _Setup the sliders on the left sidebar 
                according to your situation_""")

    f = 1 - (1-(p))**N

    st.markdown('#### $\\Longrightarrow$ Results:')

    st.info(f"""Proportion of cases in population $p = {p*100:.3f}\%$ 
            \nCommuters encountered during a round trip commute $N \\approx$ {N:.0f}
            \nYour est. prob. of encountering a contagious cough or cold during 
             the daily round trip commute is: $P(X>0) = {f*100:.1f}\\%$""")
    
    f5 = 1 - (1-f)**5
    days= 'days'

    st.info(f"""... and over a 5 day week: $P(X>0|5 \, days) 
                = 1 - (1-f)^5 = {f5*100:.1f}\\%$""")

    st.markdown('---')
    st.markdown("""<sub>\** NOTE: This naive model is only to illustrate the power 
                of social separation, and makes no attempt to model 
                case discovery rates / transmission rates or vectors / 
                crowd dynamics / self quarantine etc.
                **Do not use this for anything!**</sub>""",
                unsafe_allow_html=True)



if __name__ == "__main__":
    main()