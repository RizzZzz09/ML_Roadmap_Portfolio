def main():
    emails = ["a@mail.com", "b@gmail.com", "c@mail.com", "d@sub.domain.org", "e@gmail.com"]
    unique_domains = {email.split("@")[1] for email in emails}

    print(unique_domains)


if __name__ == "__main__":
    main()
