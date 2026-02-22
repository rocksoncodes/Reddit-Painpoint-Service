from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from pipelines.egress_pipeline import execute_egress_pipeline
from pipelines.core_pipeline import execute_core_pipeline
from pipelines.ingress_pipeline import execute_ingress_pipeline
from datetime import datetime, timedelta
from utils.logger import logger
from config import settings

notion_only = settings.CHOICE_ONE
email_only = settings.CHOICE_TWO
all_channels = settings.CHOICE_THREE


jobstores = {
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}
scheduler = BlockingScheduler(jobstores=jobstores)


def safe_execute(func):
    def wrapper():
        try:
            logger.info(f"Running {func.__name__}")
            func()
            logger.info(f"Finished {func.__name__}")
        except Exception:
            logger.exception(f"Error running {func.__name__}")
    return wrapper


def run_all_pipelines():
    """
    Runs the pipelines synchronously in the correct order:
    Ingress -> Core -> Egress
    """
    logger.info("Starting full pipeline sequence")
    safe_execute(execute_ingress_pipeline)()
    safe_execute(execute_core_pipeline)()
    safe_execute(lambda: execute_egress_pipeline(all_channels))()
    logger.info("Full pipeline sequence finished")


# Schedule every 2 weeks
scheduler.add_job(
    run_all_pipelines,
    trigger="interval",
    weeks=2,
    next_run_time=datetime.now() + timedelta(seconds=10),
    id="full_pipeline_sequence",
    replace_existing=True
)

logger.info("Agent starting. Scheduler is now running...")
scheduler.start()
