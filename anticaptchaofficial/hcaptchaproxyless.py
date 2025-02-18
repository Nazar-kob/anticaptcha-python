from anticaptchaofficial.antinetworking import *
import time


class hCaptchaProxyless(antiNetworking):
    def solve_and_return_solution(self):
        if (
            self.create_task(
                {
                    "clientKey": self.client_key,
                    "task": {
                        "type": "HCaptchaTaskProxyless",
                        "websiteURL": self.website_url,
                        "websiteKey": self.website_key,
                        "userAgent": self.user_agent,
                        "isInvisible": self.is_invisible,
                        "enterprisePayload": self.recaptcha_enterprise_payload,
                    },
                    "softId": self.soft_id,
                }
            )
            == 1
        ):
            self.log("created task with id " + str(self.task_id))
        else:
            self.log("could not create task")
            self.log(self.err_string)
            return 0
        # checking result
        time.sleep(5)
        task_result = self.wait_for_result(70)
        if task_result == 0:
            return 0
        else:
            return task_result["solution"]["gRecaptchaResponse"]
