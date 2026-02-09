import streamlit as st
from upstash_redis import Redis
from datetime import datetime, timezone, timedelta

# - CONSTANTS -----------------------------------------------------------------
DEBUG_MODE = False
TASK_DB = "Task_list"

# -- Initialization -----------------------------------------------------------
# - Session state
if "clear_btn_disabled" not in st.session_state:
    st.session_state["clear_btn_disabled"] = False

if "display_date" not in st.session_state:
    st.session_state["display_date"] = ""

# - Redis connection
redis = Redis(
    url=st.secrets["UPSTASH_URL"],
    token=st.secrets["UPSTASH_TOKEN"]
)

# - Date handling -------------------------------------------------------------
mnl_tz = timezone(timedelta(hours=8), name="Asia/Manila")
tomorrow = datetime.now(tz=mnl_tz) + timedelta(days=1)
st.session_state["display_date"] = \
    f"{tomorrow.strftime('%B %d, %Y')} - {tomorrow.strftime('%A')}"

# - Callbacks & Functions -----------------------------------------------------
def add_task():
    if new_task:
        redis.rpush(TASK_DB, new_task)
        st.session_state.new_task_k = ""

def clear_tasks():
    redis.delete(TASK_DB)

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
        if not redis.exists(TASK_DB):
            st.caption("*No tasks for tomorrow 😎*")
        else:
            for i, task in enumerate(redis.lrange(TASK_DB, 0, -1)):
                with st.container(
                        key=f"task_{i}",
                        border=True,
                        vertical_alignment="distribute"):
                    col211, col212 = st.columns([9, 1])
                    with col211:
                        st.write(task)
                    with col212:
                        if st.button("✖", key=f"delbtn_{i}"):
                            pop_this = redis.lindex(TASK_DB, i)
                            redis.lrem(TASK_DB, 1, pop_this)
                            st.rerun()

with col32:
    if redis.exists(TASK_DB):
        st.session_state["clear_btn_disabled"] = False
    else:
        st.session_state["clear_btn_disabled"] = True
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
# (3) User is able to mark a task as important. This adds an "urgent" emoji to
#     that item in the list when sent as a message.