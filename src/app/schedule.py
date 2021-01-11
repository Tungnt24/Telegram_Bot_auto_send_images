from celery.schedules import crontab
from src.configuration.scheduleconfig import Schedule

schedule_task = {
    "get-images-task-120-min": {
        "task": "src.logic.unsplash_image.execute",
        "schedule": crontab(
            minute=Schedule.minute,
            hour=Schedule.hour,
            day_of_week=Schedule.day_of_week,
            day_of_month=Schedule.day_of_month,
            month_of_year=Schedule.month,
        ),
    }
}
