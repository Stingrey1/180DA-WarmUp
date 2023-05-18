//using System.Collections;
//using System.Collections.Generic;
//using UnityEngine;

//public class throw : MonoBehaviour
//{

//    public Transform Ball;
//    public Transform Target;

//    // variables
//    private bool IsBallInHands = true;
//    private bool IsBallFlying = false;
//    private float T = 0;

//    // Update is called once per frame
//    void Update()
//    {
//        // ball in hands
//        // initialization
//        if (IsBallInHands)
//        {
//            // throw ball
//            if (Input.GetKeyUp(KeyCode.Space))
//            {
//                IsBallInHands = false;
//                IsBallFlying = true;
//                T = 0;
//            }
//        }

//        // ball in the air
//        if (IsBallFlying)
//        {
//            T += Time.deltaTime;
//            float duration = 0.66f;
//            float t01 = T / duration;

//            // moment when ball arrives at the target
//            if (t01 >= 1)
//            {
//                IsBallFlying = false;
//                Ball.GetComponent<Rigidbody>().isKinematic = false;
//            }
//        }
//    }

//    void OnTriggerEnter(Collider other)
//    {

//        if (!IsBallInHands && !IsBallFlying)
//        {
//                    IsBallInHands = true;
//            Ball.GetComponent<Rigidbody>().isKinematic = true;
//        }
//    }
//}