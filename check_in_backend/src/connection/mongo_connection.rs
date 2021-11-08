use crate::utils::config::{is_production_mode, is_testing_mode, CONFIG};
use mongodb::{options::ClientOptions, Client, Database};

lazy_static! {
    static ref CONNECTION_STRING: String = {
        if is_production_mode() {
            format!(
                "mongodb://{}:{}",
                CONFIG.production.database.host, CONFIG.production.database.port
            )
        } else if is_testing_mode() {
            format!(
                "mongodb://{}:{}",
                CONFIG.testing.database.host, CONFIG.testing.database.port
            )
        } else {
            format!(
                "mongodb://{}:{}",
                CONFIG.development.database.host, CONFIG.development.database.port
            )
        }
    };
    static ref DATABASE_NAME: String = {
        if is_production_mode() {
            CONFIG.production.database.db.clone()
        } else if is_testing_mode() {
            CONFIG.testing.database.db.clone()
        } else {
            CONFIG.development.database.db.clone()
        }
    };
}

async fn create_client() -> Result<Client, Box<dyn std::error::Error>> {
    let mut client_options = ClientOptions::parse(CONNECTION_STRING.to_owned()).await?;
    client_options.app_name = Some("check_in_database".to_string());
    Ok(Client::with_options(client_options)?)
}

pub async fn get_db_handle() -> Result<Database, Box<dyn std::error::Error>> {
    Ok(create_client()
        .await?
        .database(DATABASE_NAME.to_owned().as_str()))
}
