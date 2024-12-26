from datetime import datetime

from app.models import ProjectDonation


def invest(
    target: ProjectDonation,
    sources: list[ProjectDonation]
) -> list[ProjectDonation]:
    updated = []
    for source in sources:
        updated.append(source)
        invest_amount = min(
            target.full_amount - target.invested_amount,
            source.full_amount - source.invested_amount,
        )
        for object in (target, source):
            object.invested_amount += invest_amount
            if object.invested_amount == object.full_amount:
                object.close_date = datetime.now()
                object.fully_invested = True
        if target.fully_invested:
            break
    return updated
