use crate::entities::person;
use chrono::prelude::*;

const TIME_FORMAT: &str = "%Y-%m-%d %H:%M:%S";

pub fn get_current_time_and_add_request_millis(
    request: &person::GenerateCodeAndStartRequest,
) -> NaiveDateTime {
    let utc: DateTime<Utc> = Utc::now();
    let secs =
        utc.timestamp() + NaiveDateTime::parse_from_str(request.date_time.as_str(), TIME_FORMAT)
        .expect("Could not parse NaiveDateTime from String")
        .timestamp();
    NaiveDateTime::from_timestamp(secs, 0)
}

pub fn parse_request_time(timestamp_string: String) -> NaiveDateTime {
    NaiveDateTime::parse_from_str(timestamp_string.as_str(), TIME_FORMAT)
        .expect("Parse naive date time failed")
}

// Literally just checks which datetime is the latest
pub fn time_expired(verification_time: NaiveDateTime) -> bool {
    todo!()
}
