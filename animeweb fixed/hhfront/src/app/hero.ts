export interface Hero {
  id: number;
  name: string;
  rating: number;
  description: string;
  image: string;
}

export class LoginResponse {
  token: string;
}
