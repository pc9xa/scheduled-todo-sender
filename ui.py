from datetime import datetime, timezone, timedelta
import streamlit as st
import json

# - CONSTANTS -----------------------------------------------------------------
DEBUG_MODE = False

# -- Initialize session state -------------------------------------------------
if "to_do_list" not in st.session_state:
    st.session_state["to_do_list"] = []

if "clear_btn_disabled" not in st.session_state:
    st.session_state["clear_btn_disabled"] = False

if "display_date" not in st.session_state:
    st.session_state["display_date"] = ""

# - Date handling -------------------------------------------------------------
mnl_tz = timezone(timedelta(hours=8), name="Asia/Manila")
tomorrow = datetime.now(tz=mnl_tz) + timedelta(days=1)
st.session_state["display_date"] = \
    f"{tomorrow.strftime("%B %d, %Y")} - {tomorrow.strftime("%A")}"

# - Read tasks from json file
with open("tasks.json", "r") as task_file:
    st.session_state["to_do_list"] = json.load(task_file)

# - Callbacks & Functions -----------------------------------------------------
def add_task():
    if new_task:
        st.session_state["to_do_list"].append(new_task)
        st.session_state["save_btn_lbl"] = "Save"
        st.session_state["save_btn_disabled"] = False
        st.session_state.new_task_k = ""

        with open("tasks.json", "w") as tf:
            json.dump(st.session_state["to_do_list"], tf)

def clear_tasks():
    while st.session_state["to_do_list"]:
        st.session_state["to_do_list"].pop()

    with open("tasks.json", "w") as tf:
        json.dump(st.session_state["to_do_list"], tf)

# - CSS ----------------------------------------------------------------------
with open("style.css") as style:
    st.markdown(f"<style>{style.read()}</style>", unsafe_allow_html=True)

# - UI ------------------------------------------------------------------------
# - App Title
with st.container(border=True, key="title"):
    st.title("🌞 First Thing")
    st.caption("*Waking up to what matters.* "
               "An app that sends me my to-do list via WhatsApp every 6AM.")

# - Adding a task
col21, col22 = st.columns([8.25,1.25])
with col21:
    new_task = st.text_input(
        label="Add a task for tomorrow:",
        placeholder="Write your task here...",
        icon="📝",
        key="new_task_k",
    )
with col22:
    st.space("small")
    st.button(
        label="Add",
        disabled=not new_task,
        on_click=add_task,
        key="add_btn",
        width="stretch"
    )

# - Task list
st.write(f"> To-do List: {st.session_state["display_date"]}")
col31, col32 = st.columns([8.25,1.25])
with col31:
    with st.container(
            border=True,
            key="task_list",
            height="stretch"):
        if not st.session_state["to_do_list"]:
            st.caption("*No tasks for tomorrow 😎*")
        else:
            for i, task in enumerate(st.session_state["to_do_list"]):
                with st.container(
                        key=f"task_{i}",
                        border=True,
                        vertical_alignment="distribute"):
                    col211, col212 = st.columns([9, 1])
                    with col211:
                        st.write(task)
                    with col212:
                        if st.button("✖", key=f"delbtn_{i}"):
                            st.session_state["to_do_list"].pop(i)
                            with open("tasks.json", "w") as task_file:
                                json.dump(st.session_state["to_do_list"],
                                          task_file)
                            st.rerun()

with col32:
    if not st.session_state["to_do_list"]:
        st.session_state["clear_btn_disabled"] = True
    else:
        st.session_state["clear_btn_disabled"] = False
    st.button(
        label="Clear",
        disabled=st.session_state["clear_btn_disabled"],
        on_click=clear_tasks,
        key="clear_btn",
        width="stretch",
        help="Clear all tasks."
    )



# - Footer
st.space("large")
st.caption("by Patricia Ysabel Canencia, © 2026")

# - DEBUG CODE ----------------------------------------------------------------
if DEBUG_MODE:
    st.divider()
    # Enable the code below to clear entire session state
    # for k in st.session_state.keys():
    #     del st.session_state[k]

    # Show session state
    "[SHOW] Session state: ", st.session_state

# - DEV NOTES FOR IMPROVEMENT -------------------------------------------------
# (1) Add the task when I hit enter after typing inside text input, instead of
#     having to click outside the field, then clicking the Add button
# (2) If possible, make each task card draggable to enable the user to change
#     the order of the tasks in the list.