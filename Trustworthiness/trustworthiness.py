import numpy as np


def failed_login_trustworthiness(failed_logins):
    if failed_logins < 5:
        return 1.0
    elif failed_logins < 15:
        return 0.5
    else:
        return 0.0


def successful_login_trustworthiness(successful_logins):
    if successful_logins < 5:
        return 0.0
    elif successful_logins < 15:
        return 0.5
    else:
        return 1.0


def time_since_last_login_trustworthiness(time_elapsed):
    if time_elapsed < 1:
        return 1.0
    elif time_elapsed < 7:
        return 0.5
    else:
        return 0.0


def overall_trustworthiness(failed_logins, successful_logins, time_elapsed):
    failed_login_weight = 0.3
    successful_login_weight = 0.3
    time_elapsed_weight = 0.4

    trust_failed_logins = failed_login_trustworthiness(failed_logins)
    trust_successful_logins = successful_login_trustworthiness(successful_logins)
    trust_time_elapsed = time_since_last_login_trustworthiness(time_elapsed)

    overall_trust = (
        failed_login_weight * trust_failed_logins
        + successful_login_weight * trust_successful_logins
        + time_elapsed_weight * trust_time_elapsed
    )

    return overall_trust


failed_logins = 3
successful_logins = 7
time_elapsed = 2

trustworthiness = overall_trustworthiness(
    failed_logins, successful_logins, time_elapsed
)
print(f"Trustworthiness: {trustworthiness}")
