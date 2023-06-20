export interface Node {
  [key: string]: unknown;

  id: number;
  foo: number;
  bar: number;
  baz: number;
  qux: string;
  quux: string;
  corge: string;
  neighbors: number[];
}

export interface BaseResponse {
  data: unknown;
  status: number;
  statusText: string;
}

export interface GetNodeReponse extends BaseResponse {
  data: Node;
}

export interface GetNodesLengthResponse extends BaseResponse {
  data: number;
}
