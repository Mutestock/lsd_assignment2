use crate::{entities::user, logic::user_handler};
use user::user_server::User;
use tonic::{Request, Response, Status};

#[derive(Default)]
pub struct UserCon {}

#[tonic::async_trait]
impl User for UserCon {

    async fn login(
        &self,
        request: Request<user::LoginRequest>,
    ) -> Result<Response<user::LoginResponse>, Status> {
        println!("Got a request from {:?}", request.remote_addr());

        Ok(Response::new(
            user_handler::login(request.into_inner())
                .await
                .expect("Person Update failed"),
        ))
    }
    async fn create_user(
        &self,
        request: Request<user::CreateUserRequest>,
    ) -> Result<Response<user::CreateUserResponse>, Status> {
        println!("Got a request from {:?}", request.remote_addr());

        Ok(Response::new(
            user_handler::create_user(request.into_inner())
                .await
                .expect("Person Update failed"),
        ))
    }
}
